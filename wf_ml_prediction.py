import os
import pandas as pd
import joblib
import sys

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'models')
data_processed_path = os.path.join(base_dir, 'data_processed')
prediction_path = os.path.join(base_dir, 'predictions')

def ensure_directories():
    """Ensure necessary directories exist."""
    if not os.path.exists(prediction_path):
        os.makedirs(prediction_path)

def load_models():
    """Load all trained models"""
    models = {}
    try:
        scaler = joblib.load(os.path.join(model_path, 'scaler.joblib'))
        
        # Load all model files from the 'models' directory
        for model_file in os.listdir(model_path):
            if model_file.endswith('.joblib') and model_file != 'scaler.joblib':
                model_name = model_file.replace('.joblib', '')
                # Load the model object
                models[model_name] = joblib.load(os.path.join(model_path, model_file))
        
        return models, scaler
    except FileNotFoundError as e:
        print(f"Error loading models: {e}")
        sys.exit(1)

def load_test_data():
    """Load the saved test data for predictions."""
    X_test_scaled = pd.read_csv(os.path.join(data_processed_path, 'X_test.csv')).values
    y_test = pd.read_csv(os.path.join(data_processed_path, 'y_test.csv')).values.flatten()
    return X_test_scaled, y_test

def predict_changes():
    """Make predictions using all models"""
    # Load models and scaler
    models, _ = load_models()
    
    # Load test data
    X_test_scaled, y_test = load_test_data()
    
    # Make predictions with each model
    predictions = {}
    for name, model in models.items():
        if hasattr(model, 'predict'):  # Check if model has predict method
            model_predictions = model.predict(X_test_scaled)
            predictions[name] = {
                'predictions': model_predictions,
                'sample_predictions': {
                    'first_5_actual': y_test[:5],
                    'first_5_predicted': model_predictions[:5]
                }
            }
        else:
            print(f"Warning: Model {name} does not support prediction.")
    
    return predictions

def save_predictions(predictions):
    """Save predictions to CSV files."""
    ensure_directories()
    
    for model_name, pred_data in predictions.items():
        pred_df = pd.DataFrame({
            'Actual': pred_data['sample_predictions']['first_5_actual'],
            'Predicted': pred_data['sample_predictions']['first_5_predicted']
        })
        pred_df.to_csv(os.path.join(prediction_path, f'{model_name}_sample_predictions.csv'), index=False)

def main():
    """Main prediction workflow."""
    print("Starting Model Predictions...")
    predictions = predict_changes()
    # save_predictions(predictions)
    for model_name, pred_data in predictions.items():
        print(f"\nModel: {model_name}")
        print("First 5 Actual Values:", pred_data['sample_predictions']['first_5_actual'])
        print("First 5 Predicted Values:\n", pred_data['sample_predictions']['first_5_predicted'])

if __name__ == '__main__':
    main()

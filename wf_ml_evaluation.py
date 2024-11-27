import logging
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
import joblib
import os
import wf_ml_training
import wf_ml_prediction

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'models')
data_processed_path = os.path.join(base_dir, 'data_processed')
evaluation_path = os.path.join(base_dir, 'evaluation')
summary_file = os.path.join(base_dir, 'evaluation', 'summary.txt')

def ensure_directories():
    """Ensure necessary directories exist."""
    if not os.path.exists(evaluation_path):
        os.makedirs(evaluation_path)


# def load_models():
#     """Load all trained models."""
#     models = {}
#     for model_file in os.listdir(model_path):
#         if model_file.endswith('.joblib') and model_file != 'scaler.joblib':
#             model_name = model_file.replace('.joblib', '')
#             models[model_name] = joblib.load(os.path.join(model_path, model_file))
#     return models

# def load_test_data():
#     """Load the saved test data."""
#     X_test_scaled = pd.read_csv(os.path.join(data_processed_path, 'X_test.csv')).values
#     y_test = pd.read_csv(os.path.join(data_processed_path, 'y_test.csv')).values.flatten()
#     return X_test_scaled, y_test

def load_data():
    """Load training and test data"""
    X_train = pd.read_csv(os.path.join(data_processed_path, 'X_train.csv')).values 
    X_test = pd.read_csv(os.path.join(data_processed_path, 'X_test.csv')).values  
    y_train = pd.read_csv(os.path.join(data_processed_path, 'y_train.csv')).values 
    y_test = pd.read_csv(os.path.join(data_processed_path, 'y_test.csv')).values  
    
    return X_train, X_test, y_train, y_test

def construct_alternative_models(X_train, y_train):
    """Construct alternative models with different configurations"""
    
    # Alternative 1: Linear Regression
    ridge_model = Ridge(alpha=0.1)
    # Alternative 2: Ridge Regression (with alpha tuning)
    lasso_model = Lasso(alpha=0.1)
    # Alternative 4: KNN Regressor (different values of k)
    knn_model_1 = KNeighborsRegressor(n_neighbors=3)
    knn_model_2 = KNeighborsRegressor(n_neighbors=10)
    
    # Fit models
    ridge_model.fit(X_train, y_train)
    lasso_model.fit(X_train, y_train)
    knn_model_1.fit(X_train, y_train)
    knn_model_2.fit(X_train, y_train)
    
    models = {
        'Ridge Regression (alpha = 0.1)': ridge_model,
        'Lasso Regression': lasso_model,
        'KNN (k=3)': knn_model_1,
        'KNN (k=10)': knn_model_2
    }

    for name, model in models.items():
        model.fit(X_train, y_train)  # Train the model
        
        # Define the path where the model will be saved
        model_save_path = os.path.join(model_path, f'{name}.joblib')
        
        # Save the trained model using joblib
        joblib.dump(model, model_save_path)
    
    return models

def evaluate_models():

    if not os.path.exists(evaluation_path):
        os.makedirs(evaluation_path)
    """Evaluate multiple models and save the results"""
    # Load data
    X_train, X_test, y_train, y_test = load_data()
    
    # Construct alternative models
    models = construct_alternative_models(X_train, y_train)
    
    # Prepare a list to store results
    results = []
    
    # Evaluate each model
    for name, model in models.items():
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        
        # Store results in a dictionary
        results.append({
            'model_name': name,
            'mean_squared_error': mse,
            'root_mean_squared_error': rmse,
            'r_squared': r2,
            'mean_absolute_error': mae,
        })
    
    if not results:
        logging.error("No results to evaluate. Check if models were loaded and evaluated correctly.")
        return
    
    # Write results to a file
    with open(summary_file, 'w') as f:
        f.write(f"Model Evaluation Summary\n")
        f.write("=" * 80 + "\n\n")
        
        # Create header, including 'model_name'
        metrics = list(results[0].keys())  # Include 'model_name' in the header
        header = "| " + " | ".join(f"{m:^25}" for m in metrics) + " |"
        separator = "|" + "|".join("-" * 27 for _ in metrics) + "|"
        
        f.write(header + "\n")
        f.write(separator + "\n")
        
        # Write results, ensuring model name is first
        for result in results:
            row = "| " + " | ".join(
                f"{str(result[m]):^25}" if m == 'model_name' else f"{result[m]:^25.4f}"
                for m in metrics
            ) + " |"
            f.write(row + "\n")

    logging.info(f"Evaluation results saved to {summary_file}")

# def evaluate_models():
#     """Evaluate models and save results."""
#     ensure_directories()
#     models = load_models()
#     X_test_scaled, y_test = load_test_data()
    
#     results = []
#     for name, model in models.items():
#         y_pred = model.predict(X_test_scaled)
        
#         mse = mean_squared_error(y_test, y_pred)
#         rmse = np.sqrt(mse)
#         r2 = r2_score(y_test, y_pred)
#         mae = mean_absolute_error(y_test, y_pred)
        
#         results.append({
#             'model_name': name,
#             'mean_squared_error': mse,
#             'root_mean_squared_error': rmse,
#             'r_squared': r2,
#             'mean_absolute_error': mae,
#         })
    
#     results_df = pd.DataFrame(results)
#     results_df.to_csv(os.path.join(evaluation_path, 'model_evaluation.csv'), index=False)
#     print("Evaluation completed. Results saved.")

def main():
    """Main evaluation workflow."""
    print("\nStarting training...")
    wf_ml_training.main()
    print("Model training and saving completed.")
    wf_ml_prediction.main()
    evaluate_models()

if __name__ == '__main__':
    main()
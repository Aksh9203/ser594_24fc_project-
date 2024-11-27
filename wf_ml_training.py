import os
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import numpy as np

# Define paths
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'models')
data_processed_path = os.path.join(base_dir, 'data_processed')

def ensure_directories():
    """Ensure necessary directories exist."""
    directories = ['models', 'data_processed']
    for dir_path in directories:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

def load_and_clean_data():
    """Load and preprocess the ATP dataset."""
    data = pd.read_csv(os.path.join(data_processed_path, 'cleaned_atp_data.csv'))
    
    # Remove irrelevant columns
    data = data.drop(columns=['Tournament', 'Date', 'Series', 'Court', 'Surface', 'Round', 'Best of', 'Score'], errors='ignore')
    
    # Handle missing values for numeric columns only
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
    
    # Handle missing values for non-numeric columns (if any strategy is needed)
    # For example, you could fill categorical missing values with a placeholder or mode:
    # data['Player_1'] = data['Player_1'].fillna('Unknown')
    
    return data

def prepare_features(data):
    """Prepare features and target variable."""
    X = data[['Rank_1', 'Rank_2', 'Pts_1', 'Pts_2', 'Odd_1', 'Odd_2', 'Player_1', 'Player_2']]
    y = data['Winner']  # The target is the 'Winner' column
    
    return X, y

from sklearn.preprocessing import StandardScaler, LabelEncoder

def split():
    # Create models directory if it doesn't exist
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    
    # Load and prepare data
    data = load_and_clean_data()
    
    # Identify categorical columns (e.g., player names)
    categorical_columns = ['Player_1', 'Player_2', 'Winner']  # Replace with your actual categorical column names
    
    # Encode categorical columns
    label_encoders = {}
    for col in categorical_columns:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col])
        label_encoders[col] = le  # Store the encoder if you need to inverse transform later
    
    # Prepare features and target variable
    X, y = prepare_features(data)
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features (only after encoding)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save scaled data
    pd.DataFrame(X_train_scaled).to_csv(os.path.join(data_processed_path, 'X_train.csv'), index=False)
    pd.DataFrame(X_test_scaled).to_csv(os.path.join(data_processed_path, 'X_test.csv'), index=False)
    pd.DataFrame(y_train).to_csv(os.path.join(data_processed_path, 'y_train.csv'), index=False)
    pd.DataFrame(y_test).to_csv(os.path.join(data_processed_path, 'y_test.csv'), index=False)
    
    # Save the scaler and label encoders for future use
    joblib.dump(scaler, os.path.join(model_path, 'scaler.joblib'))
    
    return X_train_scaled, y_train

def train_models(X_train, y_train):
    """Train multiple models and save them to the specified directory."""
    models = {
        'linear_regression': LinearRegression(),
        # 'ridge_regression': Ridge(alpha=1.0),
        # 'lasso_regression': Lasso(alpha=1.0)
    }
    
    for name, model in models.items():
        print(f"Training model: {name}")
        model.fit(X_train, y_train)
        
        # Save the model
        model_save_path = os.path.join(model_path, f'{name}.joblib')
        joblib.dump(model, model_save_path)
        print(f"{name} model saved to {model_save_path}")

    print("Model has been trained and saved successfully!")

def main():
    """Main training workflow."""
    ensure_directories()
    X_train, y_train = split()
    train_models(X_train, y_train)

if __name__ == '__main__':
    main()
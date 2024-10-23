import pandas as pd
import os

def process_data():
    # Load dataset
    file_path = 'data_original/atp_tennis.csv'
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}")
    else:
        print(f"File {file_path} not found!")
        return

    # Example cleaning: Handle rows with -1 values
    print("Original data shape:", data.shape)
    
    # Check if there are any -1 values in the data
    if (data == -1).any().any():
        print("Found -1 values, cleaning data...")
    else:
        print("No -1 values found in the dataset.")
    
    # Remove rows where any column contains -1
    data_cleaned = data[~(data == -1).any(axis=1)]
    print(f"Cleaned data shape: {data_cleaned.shape}")

    # Drop duplicates (if needed)
    data_cleaned.drop_duplicates(inplace=True)

    # Get absolute path for data_preprocessing/data_processed folder
    preprocessing_dir = os.path.join(os.getcwd(), 'data_preprocessing')
    processed_data_dir = os.path.join(preprocessing_dir, 'data_processed')

    # Create 'data_preprocessing' and 'data_processed' folder if they don't exist
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
        print(f"Created directory: {processed_data_dir}")

    # Save processed data in the data_preprocessing/data_processed folder
    processed_file_path = os.path.join(processed_data_dir, 'cleaned_atp_data.csv')
    data_cleaned.to_csv(processed_file_path, index=False)

    print("Processed data saved:", processed_file_path)

# Run the processing function
process_data()

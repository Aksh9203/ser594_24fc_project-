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

    print("Original data shape:", data.shape)

    # Filter data to keep only Australian Open and Wimbledon rows
    selected_tournaments = ['Australian Open', 'Wimbledon']
    data_filtered = data[data['Tournament'].isin(selected_tournaments)]
    print(f"Data shape after filtering tournaments: {data_filtered.shape}")

    # Remove rows where any column contains -1
    data_cleaned = data_filtered[~(data_filtered == -1).any(axis=1)]
    print(f"Data shape after removing rows with -1: {data_cleaned.shape}")

    # Drop duplicates (if needed)
    data_cleaned.drop_duplicates(inplace=True)

    # Define the output folder and file path
    processed_data_dir = os.path.join(os.getcwd(), 'data_processed')
    processed_file_path = os.path.join(processed_data_dir, 'cleaned_atp_data.csv')

    # Create directories if they don't exist
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
        print(f"Created directory: {processed_data_dir}")

    # Save processed data in the 'data_processed' folder
    data_cleaned.to_csv(processed_file_path, index=False)

    print(f"Processed data saved at: {processed_file_path}")

# Run the processing function
process_data()

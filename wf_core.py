import os
import pandas as pd
import wf_visualization
import wf_ml_evaluation

def check_environment():
    """Check if required directories exist."""
    required_dirs = ['data_original', 'data_processed', 'visuals']
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory
    
    for dir_name in required_dirs:
        dir_path = os.path.join(base_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            print(f"Created directory: {dir_path}")

def process_data():
    """Process the ATP tennis dataset."""
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

    # Safely delete the existing file if it exists
    if os.path.exists(processed_file_path):
        os.remove(processed_file_path)
        print(f"Deleted existing file: {processed_file_path}")

    # Save processed data in the 'data_processed' folder
    data_cleaned.to_csv(processed_file_path, index=False)

    print(f"Processed data saved at: {processed_file_path}")

def main():
    """Main workflow execution."""
    try:
        print("Checking environment...")
        check_environment()
        
        print("\nStarting data processing...")
        process_data()
        
        print("\nStarting visualization...")
        wf_visualization.main()

        print("\nStarting evaluation...")
        wf_ml_evaluation.main()
        
        print("\nWorkflow completed successfully!")
        
    except Exception as e:
        print(f"\nError in workflow execution: {str(e)}")
        print("\nPlease ensure:")
        print("1. The raw data file 'atp_tennis.csv' is placed in the 'data_original' directory.")
        print("2. All required Python packages are installed (pandas, seaborn, matplotlib).")
        raise

if __name__ == "__main__":
    main()

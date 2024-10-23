import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

# -------------------- Data Preprocessing --------------------

def process_data():
    """Load, clean, and save the ATP dataset."""
    file_path = 'data_original/atp_tennis.csv'
    
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        print(f"Loaded data from {file_path}")
    else:
        print(f"File {file_path} not found!")
        return

    print("Original data shape:", data.shape)

    if (data == -1).any().any():
        print("Found -1 values, cleaning data...")
    else:
        print("No -1 values found in the dataset.")

    data_cleaned = data[~(data == -1).any(axis=1)]
    print(f"Cleaned data shape: {data_cleaned.shape}")

    # Drop duplicates safely
    data_cleaned = data_cleaned.drop_duplicates()

    # Define directories
    preprocessing_dir = os.path.join(os.getcwd(), 'data_preprocessing')
    processed_data_dir = os.path.join(preprocessing_dir, 'data_processed')

    os.makedirs(processed_data_dir, exist_ok=True)

    # Save to a temporary file
    temp_file_path = os.path.join(processed_data_dir, 'temp_cleaned_atp_data.csv')
    processed_file_path = os.path.join(processed_data_dir, 'cleaned_atp_data.csv')

    data_cleaned.to_csv(temp_file_path, index=False)  # Save to temporary file
    
    # Delete existing processed file if it exists
    if os.path.exists(processed_file_path):
        os.remove(processed_file_path)

    os.rename(temp_file_path, processed_file_path)  # Safely rename

    print("Processed data saved:", processed_file_path)

# -------------------- Data Visualization --------------------

def load_data():
    """Load the cleaned ATP dataset."""
    project_root = os.path.dirname(__file__)
    data_path = os.path.join(project_root, "data_preprocessing", "data_processed", "cleaned_atp_data.csv")
    
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"Dataset not found at {data_path}. Please ensure the file exists.")
    
    return pd.read_csv(data_path)

def get_feature_types(data):
    """Categorize columns into quantitative and qualitative features."""
    quantitative = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    qualitative = data.select_dtypes(include=['object', 'category']).columns.tolist()
    return quantitative, qualitative

def plot_scatter(data, quantitative, output_dir):
    """Generate scatter plots for quantitative features."""
    for i, feature_x in enumerate(quantitative):
        for feature_y in quantitative[i + 1:]:
            plt.figure(figsize=(8, 6))
            sns.scatterplot(data=data, x=feature_x, y=feature_y, alpha=0.6, edgecolor='w')
            plt.title(f'Scatter Plot: {feature_x} vs {feature_y}', fontsize=14)
            plt.xlabel(feature_x, fontsize=12)
            plt.ylabel(feature_y, fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            filename = os.path.join(output_dir, f"{feature_x}_vs_{feature_y}.png")
            plt.savefig(filename)
            plt.close()

def plot_histograms(data, qualitative, output_dir):
    """Generate histograms for qualitative features."""
    for feature in qualitative:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x=feature, palette='muted')
        plt.title(f'Histogram of {feature}', fontsize=14)
        plt.xlabel(feature, fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()
        filename = os.path.join(output_dir, f"histogram_{feature}.png")
        plt.savefig(filename)
        plt.close()

def save_summary(data, output_dir):
    """Save summary statistics."""
    quantitative, qualitative = get_feature_types(data)

    summary_file = os.path.join(output_dir, "summary.txt")
    with open(summary_file, 'w') as f:
        f.write("Summary Statistics\n")
        f.write("------------------\n")

        for feature in quantitative:
            f.write(f"\nQuantitative Feature: {feature}\n")
            f.write(f"Min: {data[feature].min()}\n")
            f.write(f"Max: {data[feature].max()}\n")
            f.write(f"Median: {data[feature].median()}\n")

        for feature in qualitative:
            category_counts = data[feature].value_counts()
            f.write(f"\nQualitative Feature: {feature}\n")
            f.write(f"Number of Categories: {len(category_counts)}\n")
            f.write(f"Most Frequent: {category_counts.idxmax()} ({category_counts.max()} occurrences)\n")
            f.write(f"Least Frequent: {category_counts.idxmin()} ({category_counts.min()} occurrences)\n")
    
    print(f"Summary statistics saved to: {summary_file}")

def save_correlations(data, output_dir):
    """Save correlation matrix."""
    quantitative, _ = get_feature_types(data)
    correlation_matrix = data[quantitative].corr()

    correlation_file = os.path.join(output_dir, "correlations.txt")
    with open(correlation_file, 'w') as f:
        f.write("Correlation Matrix\n")
        f.write("------------------\n")
        f.write(correlation_matrix.to_string())

    print(f"Correlation matrix saved to: {correlation_file}")

# -------------------- Main Function --------------------

def main():
    """Main entry point for the script."""
    project_root = os.path.dirname(__file__)
    visuals_dir = os.path.join(project_root, "visuals")
    processed_data_dir = os.path.join(project_root, "data_preprocessing", "data_processed")

    os.makedirs(visuals_dir, exist_ok=True)
    os.makedirs(processed_data_dir, exist_ok=True)

    print("Processing data...")
    process_data()

    print("Loading data...")
    data = load_data()
    quantitative, qualitative = get_feature_types(data)

    print("Generating scatter plots...")
    plot_scatter(data, quantitative, visuals_dir)

    print("Generating histograms...")
    plot_histograms(data, qualitative, visuals_dir)

    print("Saving summary statistics...")
    save_summary(data, processed_data_dir)

    print("Saving correlation matrix...")
    save_correlations(data, processed_data_dir)

    print(f"All plots and reports saved to: {visuals_dir} and {processed_data_dir}")

# -------------------- Entry Point --------------------

if __name__ == "__main__":
    main()

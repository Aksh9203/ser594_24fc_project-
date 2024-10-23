import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    """Load the cleaned ATP dataset from the data_processed directory."""
    project_root = os.path.dirname(__file__)  # Directory of this script
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
    """Generate scatter plots for each pair of quantitative features."""
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
    """Generate histograms for each qualitative feature."""
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
    """Save summary statistics to summary.txt."""
    quantitative, qualitative = get_feature_types(data)

    summary_file = os.path.join(output_dir, "summary.txt")
    with open(summary_file, 'w') as f:
        f.write("Summary Statistics\n")
        f.write("------------------\n")

        # Summary for quantitative features (min, max, median)
        for feature in quantitative:
            f.write(f"\nQuantitative Feature: {feature}\n")
            f.write(f"Min: {data[feature].min()}\n")
            f.write(f"Max: {data[feature].max()}\n")
            f.write(f"Median: {data[feature].median()}\n")

        # Summary for qualitative features (number of categories, most and least frequent)
        for feature in qualitative:
            f.write(f"\nQualitative Feature: {feature}\n")
            category_counts = data[feature].value_counts()
            f.write(f"Number of Categories: {len(category_counts)}\n")
            f.write(f"Most Frequent: {category_counts.idxmax()} ({category_counts.max()} occurrences)\n")
            f.write(f"Least Frequent: {category_counts.idxmin()} ({category_counts.min()} occurrences)\n")
    
    print(f"Summary statistics saved to: {summary_file}")

def save_correlations(data, output_dir):
    """Save correlation matrix to correlations.txt."""
    quantitative, _ = get_feature_types(data)
    correlation_matrix = data[quantitative].corr()

    correlation_file = os.path.join(output_dir, "correlations.txt")
    with open(correlation_file, 'w') as f:
        f.write("Correlation Matrix\n")
        f.write("------------------\n")
        f.write(correlation_matrix.to_string())

    print(f"Correlation matrix saved to: {correlation_file}")

def main():
    # Define output directories.
    project_root = os.path.dirname(__file__)  # Directory of this script
    visuals_dir = os.path.join(project_root, "visuals")
    processed_data_dir = os.path.join(project_root, "data_preprocessing", "data_processed")

    os.makedirs(visuals_dir, exist_ok=True)  # Create visuals folder if it doesn't exist
    os.makedirs(processed_data_dir, exist_ok=True)  # Create data_processed folder if it doesn't exist

    # Load data and determine feature types.
    print("Loading data...")
    data = load_data()
    quantitative, qualitative = get_feature_types(data)

    # Generate scatter plots.
    print("Generating scatter plots...")
    plot_scatter(data, quantitative, visuals_dir)

    # Generate histograms.
    print("Generating histograms...")
    plot_histograms(data, qualitative, visuals_dir)

    # Save summary statistics.
    print("Saving summary statistics...")
    save_summary(data, processed_data_dir)

    # Save correlation matrix.
    print("Saving correlation matrix...")
    save_correlations(data, processed_data_dir)

    print(f"All plots and reports saved to: {visuals_dir} and {processed_data_dir}")

if __name__ == "__main__":
    main()

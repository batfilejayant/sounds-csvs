import os
import pandas as pd

def merge_csvs_from_directories(dir1, dir2, output_file):
    # Initialize an empty list to hold all dataframes
    all_dataframes = []
    
    # Function to collect all CSV files in a given directory, ignoring specific ones
    def collect_csvs_from_directory(directory):
        for root, _, files in os.walk(directory):
            for file in files:
                # Ignore CSV files that end with "rows.csv" or start with "Processed"
                if file.endswith("rows.csv") or file.startswith("Processed"):
                    print(f"Ignoring file: {file}")
                    continue
                
                # Process the valid CSV files
                if file.endswith(".csv"):
                    file_path = os.path.join(root, file)
                    print(f"Processing file: {file_path}")
                    try:
                        # Skip bad lines and handle varying field counts
                        df = pd.read_csv(file_path, on_bad_lines='skip')
                        all_dataframes.append(df)
                    except pd.errors.ParserError as e:
                        print(f"Error processing {file_path}: {e}")
    
    # Collect CSVs from both directories
    collect_csvs_from_directory(dir1)
    collect_csvs_from_directory(dir2)
    
    # Concatenate all collected DataFrames
    merged_df = pd.concat(all_dataframes, ignore_index=True)
    
    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(output_file, index=False)
    print(f"All CSVs merged into: {output_file}")

# Set your directories
dir1 = "emergency sounds"
dir2 = "normal sounds"
output_file = "merged_output.csv"

merge_csvs_from_directories(dir1, dir2, output_file)

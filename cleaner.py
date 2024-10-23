import os
import pandas as pd

def process_csv(input_file: str, output_file: str, delimiter: str = ';', pos_labels_idx: int = 3) -> pd.DataFrame:
    # Read the dataset with specified delimiter and skip the first row
    df = pd.read_csv(input_file, delimiter=delimiter, skiprows=1, header=None)

    # Set the second row as header and remove the first row
    df.columns = df.iloc[0]
    df = df.drop(0)

    # Split the first column into four distinct columns based on commas
    df = df[df.columns[0]].str.split(',', expand=True)

    # Drop rows containing "#NAME?" in the first column
    df = df[df.iloc[:, 0] != "#NAME?"]

    # Reset the index
    df = df.reset_index(drop=True)

    # Reset the first row as the header
    df.columns = df.iloc[0]
    df = df.drop(0)

    # Merge all columns after 'positive labels' into 'positive labels' column itself
    df.iloc[:, pos_labels_idx] = df.iloc[:, pos_labels_idx].astype(str) + ',' + df.iloc[:, pos_labels_idx + 1:].apply(lambda row: ','.join(row.dropna()), axis=1)

    # Keep only the relevant columns
    df = df.iloc[:, :pos_labels_idx + 1]

    # Save the processed DataFrame to a new CSV file
    df.to_csv(output_file, index=False)

    return df

def process_all_csvs_in_folders(main_folders: list, delimiter: str = ';', pos_labels_idx: int = 3):
    for main_folder in main_folders:
        # Walk through each directory, subdirectory, and file
        for dirpath, _, files in os.walk(main_folder):
            for filename in files:
                if filename.endswith('.csv'):
                    input_file = os.path.join(dirpath, filename)
                    output_file = os.path.join(dirpath, f'Processed_{filename}')
                    process_csv(input_file, output_file, delimiter, pos_labels_idx)

# Example usage
main_folders = ['D:/college/Capstone Project/emergency sounds', 'D:/college/Capstone Project/normal sounds']  # Replace with your folder paths
process_all_csvs_in_folders(main_folders)

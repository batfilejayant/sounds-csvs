import os
import pandas as pd

def process_files_in_directory(directory):
    # Find the CSVs with "Processed" in their names and those ending with "random_rows.csv"
    processed_file = None
    random_rows_file = None

    for file in os.listdir(directory):
        if "Processed" in file and file.endswith(".csv"):
            processed_file = os.path.join(directory, file)
        elif file.endswith("random_rows.csv"):
            random_rows_file = os.path.join(directory, file)

    if not processed_file or not random_rows_file:
        print(f"Could not find required CSVs in {directory}")
        return

    # Read both CSVs into DataFrames
    processed_df = pd.read_csv(processed_file)
    random_rows_df = pd.read_csv(random_rows_file)

    # Subtract rows in random_rows from processed
    result_df = pd.concat([processed_df, random_rows_df]).drop_duplicates(keep=False)

    # Save the result to a new CSV named 'download.csv'
    output_file = os.path.join(directory, 'download.csv')
    result_df.to_csv(output_file, index=False)
    print(f"Saved result to {output_file} in directory: {directory}")

def iterate_folders(main_folders):
    for main_folder in main_folders:
        for root, dirs, files in os.walk(main_folder):
            for directory in dirs:
                dir_path = os.path.join(root, directory)
                print(f"Processing directory: {dir_path}")
                process_files_in_directory(dir_path)

def main():
    # Define the paths of two main folders
    main_folder1 = './emergency sounds'
    main_folder2 = './normal sounds'

    # Iterate over the directories in both main folders
    main_folders = [main_folder1, main_folder2]
    iterate_folders(main_folders)

if __name__ == "__main__":
    main()

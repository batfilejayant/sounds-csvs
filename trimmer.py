import os
import pandas as pd

def trim_csv_files(folder1, folder2):
    # Loop through each main folder
    for main_folder in [folder1, folder2]:
        # Walk through each subdirectory in the main folder
        for root, dirs, files in os.walk(main_folder):
            # Check if "download.csv" is in the files
            if "download.csv" in files:
                file_path = os.path.join(root, "download.csv")
                # Load the CSV file
                df = pd.read_csv(file_path)
                # Keep only the first 1000 rows
                df_trimmed = df.head(1000)
                # Overwrite the original file with the trimmed DataFrame
                df_trimmed.to_csv(file_path, index=False)
                print(f"Trimmed and updated: {file_path}")

# Specify the paths to your main folders
main_folder1 = './emergency sounds'
main_folder2 = './normal sounds'

# Call the function
trim_csv_files(main_folder1, main_folder2)

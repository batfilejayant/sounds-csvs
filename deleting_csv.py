import os

def rename_processed_csvs(directory):
    # Loop through all entries in the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Check if the file is a CSV and starts with 'processed_' (case-insensitive)
            if filename.lower().startswith('processed_') and filename.endswith('.csv'):
                # Create the new filename by removing 'processed_' from the start
                new_filename = filename[len('processed_'):]

                # Create the full path for the old and new filenames
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} to {new_file_path}")

# Example usage
main_folder1 = './emergency sounds'  # Change this to your first main folder
main_folder2 = './normal sounds'  # Change this to your second main folder

rename_processed_csvs(main_folder1)
rename_processed_csvs(main_folder2)
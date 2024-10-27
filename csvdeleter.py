import os

def delete_download_csv(folder1, folder2):
    # Loop through each main folder
    for main_folder in [folder1, folder2]:
        # Walk through each subdirectory in the main folder
        for root, dirs, files in os.walk(main_folder):
            # Check if "download.csv" is in the files
            if "download.csv" in files:
                # Construct the full path to the file
                file_path = os.path.join(root, "download.csv")
                # Delete the file
                os.remove(file_path)
                print(f"Deleted: {file_path}")

# Specify the paths to your main folders
main_folder1 = './emergency sounds'
main_folder2 = './normal sounds'

# Call the function
delete_download_csv(main_folder1, main_folder2)

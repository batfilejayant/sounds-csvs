import os
import csv

def count_files_in_directory(directory):
    """Counts files in each subdirectory within the given directory."""
    dir_file_counts = []
    
    # Walk through all subdirectories and files in the directory
    for root, dirs, files in os.walk(directory):
        file_count = len(files)
        dir_file_counts.append([root, file_count])
    
    return dir_file_counts

def generate_csv_for_directory_counts(folder1, folder2, output_csv):
    """Generates a CSV file with file counts for each subdirectory in two main folders."""
    all_counts = []

    # Get file counts for both folders
    all_counts.extend(count_files_in_directory(folder1))
    all_counts.extend(count_files_in_directory(folder2))
    
    # Write to CSV file
    with open(output_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Directory", "File Count"])  # Header row
        writer.writerows(all_counts)
    
    print(f"CSV report generated: {output_csv}")

# Paths to the two main folders
folder1 = './emergency sounds'  # Replace with the actual path
folder2 = './normal sounds'  # Replace with the actual path
output_csv = 'directory_file_counts.csv'  # Output CSV file name

# Generate the CSV report
generate_csv_for_directory_counts(folder1, folder2, output_csv)

import os
import csv
from collections import defaultdict

def find_wav_files(main_folder):
    wav_files = defaultdict(list)  # To store file name as key and list of paths as values
    
    # Walk through all directories and files in the main folder
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            if file.endswith('.wav'):
                wav_files[file].append(os.path.join(root, file))
    
    return wav_files

def find_common_wav_files(main_folder1, main_folder2):
    # Find wav files in both folders
    wav_files1 = find_wav_files(main_folder1)
    wav_files2 = find_wav_files(main_folder2)
    
    # Find common file names in both folders
    common_files = set(wav_files1.keys()) & set(wav_files2.keys())
    
    common_wav_info = []
    
    for file in common_files:
        # Combine the locations from both folders
        locations = wav_files1[file] + wav_files2[file]
        common_wav_info.append({
            'file_name': file,
            'occurrences': len(locations),
            'locations': ', '.join(locations)  # Joining locations into a single string
        })
    
    return common_wav_info

def write_common_wav_to_csv(common_wav_info, output_csv):
    # Write the results to a CSV file
    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['file_name', 'occurrences', 'locations']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for info in common_wav_info:
            writer.writerow(info)

def main():
    # Define the paths of two main folders
    main_folder1 = 'D:/Capstone Project/emergency sounds/Bang'  # Path to the first main folder
    main_folder2 = 'D:/Capstone Project/emergency sounds/Air horn, truck horn'  # Path to the second main folder

    # Find common wav files and their information
    common_wav_info = find_common_wav_files(main_folder1, main_folder2)
    
    # Output CSV file for common wav files
    output_csv = 'common_wav_files.csv'
    write_common_wav_to_csv(common_wav_info, output_csv)
    
    print(f"CSV of common wav files created: {output_csv}")

if __name__ == "__main__":
    main()

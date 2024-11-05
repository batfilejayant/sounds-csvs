import yt_dlp
from pydub import AudioSegment
import os
import csv
from concurrent.futures import ProcessPoolExecutor, as_completed

def get_video_id(url):
    return url.split('v=')[1]

def count_files_in_directory(directory):
    """Count the number of files in a directory."""
    return sum(len(files) for _, _, files in os.walk(directory))

def extract_audio_segment(video_id, start_time, end_time, output_folder):
    # Check if the total number of files in the output folder is less than 1004
    if count_files_in_directory(output_folder) >= 1004:
        print(f"Total number of files in {output_folder} has reached or exceeded 1004. Skipping video {video_id}.")
        return

    # yt-dlp options to download the best audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'wav',
        'outtmpl': f'{output_folder}/{video_id}.%(ext)s',  # Save in the CSV folder
        'ffmpeg_location': 'C:/ffmpeg',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    # Download the audio
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=True)
            audio_file = f"{output_folder}/{video_id}.wav"

        # Load the audio file and trim it using Pydub
        audio = AudioSegment.from_wav(audio_file)
        start_time_ms = start_time * 1000  # Convert to milliseconds
        end_time_ms = end_time * 1000

        trimmed_audio = audio[start_time_ms:end_time_ms]

        # Export the trimmed audio back to the same file or a new file
        trimmed_audio.export(audio_file, format="wav")
        print(f"Trimmed audio saved as: {audio_file}")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error processing video {video_id}: {str(e)}")

def process_csv(csv_file):
    csv_folder = os.path.dirname(csv_file)
    tasks = []

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("CSV Headers:", reader.fieldnames)

        for row in reader:
            video_id = row['# YTID'].strip()
            try:
                start_time = float(row[' start_seconds'].strip())
                end_time = float(row[' end_seconds'].strip())
                tasks.append((video_id, start_time, end_time, csv_folder))
            except ValueError:
                print(f"Skipping video {video_id}: Invalid start or end time.")
                continue

    # Parallel processing
    with ProcessPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(extract_audio_segment, *task) for task in tasks]
        for future in as_completed(futures):
            future.result()  # Retrieve results or handle exceptions



def find_and_process_csvs(main_folder):
    # Walk through all directories and files in the main folder
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            # Check if the file starts with 'processed' and ends with '.csv'
            if file.endswith('.csv'):
                csv_path = os.path.join(root, file)
                print(f"Found CSV file: {csv_path}")
                process_csv(csv_path)

def main():
    # Define the paths of two main folders
    main_folder1 = './emergency sounds'  # Path to the first main folder
    main_folder2 = './normal sounds'      # Path to the second main folder

    # Process CSV files from both main folders
    print(f"Processing folder: {main_folder1}")
    find_and_process_csvs(main_folder1)

    print(f"Processing folder: {main_folder2}")
    find_and_process_csvs(main_folder2)

if __name__ == "__main__":
    main()
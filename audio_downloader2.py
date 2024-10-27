import yt_dlp
from pydub import AudioSegment
import os
import csv

def get_video_id(url):
    return url.split('v=')[1]

def extract_audio_segment(video_id, start_time, end_time, output_folder):
    # yt-dlp options to download the best audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'wav',
        'outtmpl': f'{output_folder}/{video_id}.%(ext)s',  # Save in the CSV folder
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
    }

    # Download the audio
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

def process_csv(csv_file):
    # Get the directory of the CSV file to save the WAV files in the same folder
    csv_folder = os.path.dirname(csv_file)

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("CSV Headers:", reader.fieldnames)
        
        for row in reader:
            video_id = row['# YTID'].strip()

            try:
                start_time = float(row[' start_seconds'].strip())
                end_time = float(row[' end_seconds'].strip())
            except ValueError:
                print(f"Skipping video {video_id}: Invalid start or end time.")
                continue

            print(f"Processing video: {video_id}, start: {start_time}, end: {end_time}")
            extract_audio_segment(video_id, start_time, end_time, csv_folder)

def main():
    # Define the path of a sample test folder with one CSV file
    test_folder = './emergency sounds'  # Path to the test folder

    # Process the single CSV file from the test folder
    print(f"Processing test folder: {test_folder}")
    find_and_process_csvs(test_folder)

if __name__ == "__main__":
    main()
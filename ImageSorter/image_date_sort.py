import os
import sys
from datetime import datetime

def sort_images_by_date(directory):
    try:
        # List all files in the specified directory
        all_files = os.listdir(directory)

        # Filter for image files (you can customize this to match your file extensions)
        image_files = [file for file in all_files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        # Create a list of (file, modification_time) tuples
        file_mod_times = [(file, os.path.getmtime(os.path.join(directory, file))) for file in image_files]

        # Sort the list by modification time (newest to oldest)
        file_mod_times.sort(key=lambda x: x[1], reverse=True)

        # Display the sorted files
        for file, mod_time in file_mod_times:
            formatted_time = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
            print(f"File: {file}, Modified Time: {formatted_time}")
    except FileNotFoundError:
        print("Directory not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python image_date_sort.py /path/to/your/images")
    else:
        directory = sys.argv[1]
        sort_images_by_date(directory)


# Image Date Sorting Python Script

This Python script allows you to sort image files in a directory based on their modification dates, arranging them from newest to oldest. This can be useful for organizing and managing your image collection.

## Prerequisites

- Python 3.x installed on your computer.

## Usage

1. **Clone or Download the Repository**: Clone this repository to your local machine or download the script directly.

2. **Open a Terminal or Command Prompt**: Open a terminal or command prompt on your computer.

3. **Navigate to the Script's Directory**: Use the `cd` command to navigate to the directory where you have saved the `image_date_sort.py` script.

4. **Run the Script**: Execute the script by running the following command, replacing `/path/to/your/images` with the full path to the directory containing your image files:

   ```bash
   python image_date_sort.py /path/to/your/images

    View Sorted Images: The script will list the image files in the specified directory, sorted by modification date (newest to oldest). It will display the file names along with their modification timestamps.

Example

For instance, to sort images in the "Screenshots" directory of the user "Scripter" on the C: drive, you can run the script as follows:

bash

python image_date_sort.py "/c/Users/r00tKiMuT/Scripter/Screenshots"

Customization

You can customize the list of supported image file extensions by modifying the image_files list in the script.
Notes

    Ensure you use Unix-style paths (forward slashes /) when specifying the directory path in the script, especially when using Git Bash on Windows.

    If the specified directory does not exist or contains no image files, the script will display a "Directory not found" message.

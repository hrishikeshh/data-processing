# Video Cropping Script

This project provides a Python script to crop the header and footer from video files. It uses the `moviepy` library for video processing.

## Requirements

- Python 3.x
- Ubuntu Server Edition 18.04 or newer

## Installation

Follow these steps to set up the environment and install the required packages:

1. **Update and Upgrade the System:**
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. **Install Python 3 and Pip:**
   ```bash
   sudo apt install python3 python3-pip
   ```

3. **Create a Virtual Environment (optional but recommended):**
   ```bash
   sudo apt install python3-venv
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. **Install Required Python Packages:**
   - Create a `requirements.txt` file with the following content:
     ```text
     moviepy==1.0.3
     numpy==1.24.3
     imageio[ffmpeg]==0.7.2
     ```
   - Install packages:
     ```bash
     pip install -r requirements.txt
     ```

## Usage

1. **Prepare Your Folders:**
   - Place your original video files in the `original_video_data` folder.
   - Ensure you have an `output_data` folder where the cropped videos will be saved.

2. **Edit the Script:**
   - Open the `crop_video.py` script and adjust the following parameters as needed:
     - `input_folder`: Directory where your original videos are stored.
     - `output_folder`: Directory where the cropped videos will be saved.
     - `top_crop`: Number of pixels to crop from the top of the video.
     - `bottom_crop`: Number of pixels to crop from the bottom of the video.

3. **Run the Script:**
   ```bash
   python crop_video.py
   ```

   This will process all `.mp4` files in the `original_video_data` folder, crop the specified number of pixels from the top and bottom, and save the cropped videos in the `output_data` folder.

## Notes

- Ensure `ffmpeg` is installed on your system for `moviepy` to work correctly. You can install it using:
  ```bash
  sudo apt install ffmpeg
  ```
- Adjust the script for other video formats by changing the file extension in the `glob.glob` call if necessary.
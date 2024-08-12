from moviepy.editor import VideoFileClip
import os
import glob

def crop_video(input_folder, output_folder, top_crop, bottom_crop):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")

    # List all video files in the input folder
    video_files = glob.glob(f"{input_folder}/*.mp4")  # Adjust the extension as needed
    if not video_files:
        print(f"No video files found in {input_folder}")
        return

    for video_file in video_files:
        print(f"Processing file: {video_file}")

        try:
            clip = VideoFileClip(video_file)

            # Get the size of the original video
            width, height = clip.size

            # Define the cropping box
            cropping_box = (0, top_crop, width, height - bottom_crop)
            print(f"Cropping box: {cropping_box}")

            # Crop the video
            cropped_clip = clip.crop(y1=top_crop, y2=height - bottom_crop)

            # Create a new filename with 'cropped' appended
            base_name = os.path.basename(video_file)
            name, ext = os.path.splitext(base_name)
            output_file = os.path.join(output_folder, f"{name}_cropped{ext}")

            # Save the cropped video to the output folder
            cropped_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')

            print(f"Saved cropped video to: {output_file}")

            # Close the clip to free up resources
            clip.close()
            cropped_clip.close()
        except Exception as e:
            print(f"An error occurred with file {video_file}: {e}")

# Example usage
input_folder = 'data'
output_folder = 'output_data'
top_crop = 100  # Crop 100 pixels from the top
bottom_crop = 100  # Crop 100 pixels from the bottom

crop_video(input_folder, output_folder, top_crop, bottom_crop)

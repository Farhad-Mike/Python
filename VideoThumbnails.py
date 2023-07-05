#!/usr/bin/python3.9
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk  # Added for progress bar
import cv2
import os

def export_thumbnails():
    # Open file dialog to select multiple video files
    video_files = filedialog.askopenfilenames(title="Select Video Files", filetypes=(("Video files", "*.mp4;*.avi;*.ts;*.webm"), ("All files", "*.*")))
    
    # Check if video files are selected
    if video_files:
        total_videos = len(video_files)
        completed_videos = 0
        
        # Create progress bar
        progress = ttk.Progressbar(window, orient="horizontal", length=200, mode="determinate")
        progress.pack(pady=10)
        
        for video_file in video_files:
            # Open the video file
            cap = cv2.VideoCapture(video_file)
            
            # Get the total number of frames and frames per second (fps)
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            fps = cap.get(cv2.CAP_PROP_FPS)
            
            # Calculate the interval in terms of frames
            interval_frames = int(fps) * 5
            
            # Extract the video file name without extension
            video_name = os.path.splitext(os.path.basename(video_file))[0]
            
            # Initialize the current frame count and thumbnail count
            current_frame = 0
            thumbnail_count = 0
            
            # Create a directory to store the thumbnails
            thumbnail_dir = f"{video_name}_thumbnails"
            os.makedirs(thumbnail_dir, exist_ok=True)
            
            # Loop through the video frames
            while current_frame < total_frames:
                # Read the current frame
                ret, frame = cap.read()
                
                # Check if the frame is successfully read
                if ret:
                    # Check if the current frame is at the interval
                    if current_frame % interval_frames == 0:
                        # Save the thumbnail image with the video name
                        thumbnail_file = f"{thumbnail_dir}/{video_name}_thumbnail_{thumbnail_count}.jpg"
                        cv2.imwrite(thumbnail_file, frame)
                        thumbnail_count += 1
                    
                    # Increment the current frame count
                    current_frame += 1
                else:
                    break
            
            # Release the video capture
            cap.release()
            
            # Update progress bar
            completed_videos += 1
            progress["value"] = (completed_videos / total_videos) * 100
            window.update()
        
        print("Thumbnails exported successfully!")
    else:
        print("No video files selected.")

# Create the GUI window
window = tk.Tk()
window.title("Video Thumbnail Exporter")

# Create a button to trigger the export_thumbnails function
button = tk.Button(window, text="Select Videos and Export Thumbnails", command=export_thumbnails)
button.pack(padx=10, pady=10)

# Start the GUI event loop
window.mainloop()

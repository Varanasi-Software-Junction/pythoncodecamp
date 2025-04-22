import cv2
import os

def break_video_into_images(video_path, output_folder, prefix="frames"):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # No more frames

        # Save each frame as an image
        frame_filename = os.path.join(output_folder, f"{prefix}_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1

    cap.release()
    print(f"Saved {frame_count} frames to '{output_folder}'")


break_video_into_images("videos/output.mp4", "frames", prefix="output")

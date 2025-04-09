import cv2

def create_video_from_images(video_filename, image_files, fps=1):
    if not image_files:
        print("No images provided.")
        return

    # Read the first image to get the frame size
    first_frame = cv2.imread(image_files[0])
    if first_frame is None:
        print(f"Error reading image: {image_files[0]}")
        return

    height, width, _ = first_frame.shape

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(video_filename, fourcc, fps, (width, height))

    for img_path in image_files:
        frame = cv2.imread(img_path)
        if frame is None:
            print(f"Warning: Could not read image {img_path}, skipping.")
            continue
        # Resize if dimensions don't match
        if frame.shape[:2] != (height, width):
            frame = cv2.resize(frame, (width, height))
        video_writer.write(frame)

    video_writer.release()
    print(f"Video saved as {video_filename}")
create_video_from_images("videos/output.mp4",["images/numbers/0.png","images/numbers/1.png","images/numbers/2.png","images/numbers/3.png","images/numbers/4.png","images/numbers/5.png",],.5)

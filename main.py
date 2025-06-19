from app import Camera

# Defining the video path and creating an object cam for video processing purpose.
video_path = 'videos/car.mp4'
cam = Camera(video_path)

#initiating the processing.
cam.read_stream()

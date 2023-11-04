from pytube import YouTube

# Provide the URL of the YouTube video you want to download
url = "https://www.youtube.com/watch?v=qTz2ymC4XDo"

# Create a YouTube object
yt = YouTube(url)

# Get the highest resolution stream (video and audio)
video_stream = yt.streams.get_highest_resolution()

# Set the download location
download_path = "/home/user/Desktop/pytube/video"

# Download the video
video_stream.download(output_path=download_path)

print("Video downloaded successfully.")

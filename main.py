from pytube import YouTube

url = input("Enter YouTube Link: ")
videoUrl = YouTube(url)

videoDownload = videoUrl.streams.get_highest_resolution()

print("Downloading the Video: ")
videoDownload.download()
print("Video Downloaded")
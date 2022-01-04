#importing library
from pytube import YouTube

#get the url of the video 
url = input("Enter YouTube Link: ")
videoUrl = YouTube(url)

videoDownload = videoUrl.streams.get_highest_resolution()

#video downloading
print("Downloading the Video: ")
videoDownload.download()
print("Video Downloaded")
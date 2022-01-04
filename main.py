#importing library
from pytube import YouTube

#get the url of the video 
url = input("Enter YouTube Link: ")
videoUrl = YouTube(url)

print("Video Title: ", videoUrl.title) #video title
print("Video Length: ", videoUrl.length) #video length
print("No. of Views: ", videoUrl.views)  #video view
print("Thumbnail of the Video ", videoUrl.thumbnail_url) #video thumbnail

videoDownload = videoUrl.streams.get_highest_resolution()

#video downloading
print("Downloading the Video: ")
videoDownload.download()
print("Video Downloaded")
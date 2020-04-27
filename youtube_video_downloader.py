#importing required module
from pytube import YouTube
from time import sleep

#link is a variable which contains the link of the video
#which user want to download
link = input("Enter the link here:::")
yt = YouTube(link)
#title store the title of the video
title = yt.title
s = yt.streams.filter(progressive=True,file_extension='mp4')
#print the available formats
print("Available formats for >>>",title,"youtube video")
a=1
for i in s:
    print(a,end=".")
    print(i.resolution)
    a+=1

#resol contain the resolution which user want to download
resol = input("Enter any resolution from above>>")
if "p" in resol:
    userentry = resol
else:
    userentry = str(resol)+"p"
# x is the stream which user want to download
x = yt.streams.get_by_resolution(userentry)
#if x==none means that user enter a resolution that is not exists
if x==None:
    print("No resolution like this try again")
else:
    #else video will download
    print("Please wait your video is being downloading",end="")
    for i in range(4):
        print(".",end="")
        sleep(1)
    x.download()
    print("\nYour video is downloaded")
    sleep(1)
    print("Thanks for visiting us")


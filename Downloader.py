#import libraries 
from pytube import YouTube
from time import sleep
from moviepy.editor import *
import os

#create variable with method of library and URL from user
link = YouTube(
    str(input("\n\nEnter the URL: ")))

Option = input("\nPlease choose which file you want to download:\n\n1- Video     2- Audio\n\nYour choice: ")

#Download video option
if Option == "1":
    sleep(1)
    print("\nDownloading...")
#selecting video from file and saving on desktop    
    ys = link.streams.get_highest_resolution()
    out_file = ys.download(output_path = 'C:\\Users\\mivaj\\Desktop')
#changing name of new file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    os.rename(out_file, new_file)

    print("\n\n" + link.title + " has been successfully downloaded.\n")
    exit()
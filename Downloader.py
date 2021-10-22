# Import libraries 
from pytube import YouTube
from time import sleep
from moviepy.editor import *
import os

#Def method to clear screen
clear = lambda: os.system('cls')

# Create variable with method of library and URL from user
link = YouTube(
    str(input("\n\nEnter the URL: ")))

Option = input("\nWhich file would you like to save:\n\n1- Video (mp4)     2- Audio (mp3)\n\nSelect one: ")

# Download video option
if Option == "1":
    sleep(1)
    print("\nDownloading...")
# Selecting video from file and saving on desktop    
    ys = link.streams.get_highest_resolution()
    out_file = ys.download()




# Ask user for name of new file
    ChangName = input("\nWould you like to keep the original name for the new file? (Y/N):  ")
    if ChangName[0].lower() == "n":
        NewName = input("\nWhat is the new name? ")
        #base, ext = os.path.splitext(out_file)
        new_file = NewName + '.mp4'
        os.rename(out_file, new_file)    

    clear() 
    print("\n\nThe file has been successfully downloaded.\n")
    exit()

# Logic for download mp3
elif Option == "2":
    sleep(1)
    print("\nDownloading...")
    video = link.streams.filter(only_audio=True)[1]
 
# Download the file
    out_file = video.download()
   
# Ask user for name of new file
    ChangName = input("\nWould you like to keep the original name for the new file? (Y/N):  ")
    if ChangName[0].lower() == "y":
        mp4_file = out_file
        mp3_file = out_file[:-4] + ".mp3"  
    else:
        NewName = input("\nWhat is the new name? ")
        mp4_file = out_file
        mp3_file = NewName + ".mp3"       
# Converting to mp3
    audioclip = AudioFileClip(mp4_file)
    audioclip.write_audiofile(mp3_file)
    audioclip.close()

    os.remove(out_file)

# Result of success
    clear()
    print("\n\nThe file has been successfully downloaded.\n")
    exit()

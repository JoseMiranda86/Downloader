from pytube import YouTube
from time import sleep
from moviepy.editor import *
import os

link = YouTube(
    str(input("\n\nEnter the URL: ")))

Option = input("\nPlease choose which file you want to download:\n\n1- Video     2- Audio\n\nYour choice: ")
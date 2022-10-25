#!/usr/bin/env python

from moviepy.editor import *

# loading video dsa gfg intro video
clip = VideoFileClip("BigBuckBunny.mp4")

print("Enter seconds to cut: ")
N = input()

clip = clip.subclip(0, N)

clip.write_videofile("cut_video.mp4")


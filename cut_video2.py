import os
from utils import *

# Select video to apply transformation
file_name = menu()

# Select seconds to cut
N = input("Enter seconds to cut: ")

# Apply transformation using ffmpeg
command = f'ffmpeg -ss 00:00:00 -i {file_name} -t 00:00:{N} -c:v copy -c:a copy cut_video.mp4'
os.system(command)

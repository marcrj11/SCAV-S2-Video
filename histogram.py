import os
from utils import *

# Select video to apply transformation
file_name = menu()

# Apply transformation using ffmpeg
command = f'ffmpeg -i {file_name} -vf "split=2[a][b], [b]histogram, format=yuva444p[hh],' \
               '[a][hh]overlay" -c:a copy histogram_video.mp4 '
os.system(command)

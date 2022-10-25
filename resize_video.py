import os
from utils import *

# Select video to apply transformation
file_name = menu()

# Select resolution desired
resolution, new_name = resolution_menu()

# Apply transformation using ffmpeg
command = f'ffmpeg -i {file_name} -vf {resolution} {new_name}.mp4'
os.system(command)
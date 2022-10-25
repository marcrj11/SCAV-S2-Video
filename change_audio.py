import os
from utils import *

# Select video to apply transformation
file_name = menu()

# Select audio option
audio_option, new_name = audio_option_menu()

# Apply transformation using ffmpeg
command = f'ffmpeg -i {file_name} -ac {audio_option} {new_name}.mp4'
os.system(command)

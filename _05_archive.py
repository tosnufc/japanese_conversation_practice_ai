import os
import shutil
from _00_prompt import archive_folder_name

folder_name = archive_folder_name
script_source = 'conversation_scripts.txt'
script_destination = f'./archive/{folder_name}/conversation_scripts.txt'
speak_file_source = '_04_practice_speaking.py'
speak_file_destination = f'./archive/{folder_name}/practice_speaking.py'

# Create destination directory if it doesn't exist
os.makedirs(os.path.dirname(script_destination), exist_ok=True)

# Move the files
if os.path.exists(script_source):
    shutil.move(script_source, script_destination)
    print(f"{script_source} has been moved to {script_destination}")
else:
    print(f"{script_source} not found. Skipping file move.")

# Copy _04_file
shutil.copy(speak_file_source, speak_file_destination)
print(f"{speak_file_source} has been copied to {speak_file_destination}")

# Move all .mp3 files to the same destination folder
mp3_files = [f for f in os.listdir() if f.endswith('.mp3')]
for mp3_file in mp3_files:
    shutil.move(mp3_file, f'./archive/{folder_name}/{mp3_file}')
    print(f"{mp3_file} has been moved to ./archive/{folder_name}/{mp3_file}")
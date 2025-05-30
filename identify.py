import os
import shutil

# Define the directory path and file extensions
directory_path = '/path/to/your/directory'
file_extensions = {
    'Documents': ['.txt', '.docx', '.pdf'],
    'Images': ['.jpg', '.png', '.gif'],
    'Videos': ['.mp4', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.ogg']
}

# Create folders for each file type if they don't exist
for folder in file_extensions.keys():
    folder_path = os.path.join(directory_path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into their respective folders
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_extensions.items():
            if file_extension in extensions:
                destination_path = os.path.join(directory_path, folder, filename)
                shutil.move(file_path, destination_path)
                print(f"Moved {filename} to {folder} folder")
                break
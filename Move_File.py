import os
import shutil

# Set source and destination paths
from_dir = "C:/Users/Sabraham/Downloads"
to_dir = "Document_Files"

# Get list of files in the source path
list_of_files = os.listdir(from_dir)

# Print the list of files
print("List of files in the source path:")
print(list_of_files)

# Iterate through the list of files
for file_name in list_of_files:
    # Get name and extension of each file
    name, extension = os.path.splitext(file_name)

    # Skip if the extension is blank
    if not extension:
        continue

    # Check if the extension is in the specified list
    valid_extensions = ['.txt'] # Orginally these extensions: '.txt', '.doc', '.docx', '.pdf'
    if extension in valid_extensions:
        # Create paths for source, destination folder, and destination file
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)

        # Check if the destination folder exists
        if os.path.exists(path2):
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)
        else:
            # Create the destination folder
            os.makedirs(path2)
            print(f"Moving {file_name} to {path3}")
            shutil.move(path1, path3)



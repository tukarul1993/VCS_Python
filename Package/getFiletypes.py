import os
import magic

# Specify the path to the folder containing the files
folder_path = 'path/to/your/folder'

# Create a magic.Magic() object
file_type_checker = magic.Magic()

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # Check if the path points to a file
    if os.path.isfile(file_path):
        # Get the file type
        file_type = file_type_checker.from_file(file_path)

        # Print the file name and type
        print("File name:", filename)
        print("File type:", file_type)
        print()

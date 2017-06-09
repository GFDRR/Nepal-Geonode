import glob
import os

# Obtain all zip files
files = glob.glob("*.zip")

# Exclude the first two items
files_to_delete = files[2:]

for file in files_to_delete:
    # Remove file
    os.remove(file)

import os
from pathlib import Path

# Folder containing the images
folder_path = r"C:\Users\PC 9\Downloads\INTERNSHIP PYTHON"
# Prefix for new filenames
new_prefix = "Vacation"

# Supported image extensions
extensions = [".jpg", ".png"]

# Get all matching files
files = [
    file for file in Path(folder_path).iterdir()
    if file.is_file() and file.suffix.lower() in extensions
]

# Sort files for consistent numbering
files.sort()

# Rename files
for count, file in enumerate(files, start=1):
    new_name = f"{new_prefix}_{count}{file.suffix.lower()}"
    new_path = file.parent / new_name

    os.rename(file, new_path)
    print(f"Renamed: {file.name} → {new_name}")

print("All files renamed successfully!")

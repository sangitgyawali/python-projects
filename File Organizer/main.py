import os
import shutil

source_folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"],
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isdir(file_path):
        continue

    extension = os.path.splitext(file)[1].lower()

    moved = False

    for folder, extensions in file_types.items():
        if extension in extensions:
            destination = os.path.join(source_folder, folder)

            os.makedirs(destination, exist_ok=True)

            shutil.move(file_path, os.path.join(destination, file))

            print(f"Moved: {file} -> {folder}")
            moved = True
            break

    if not moved:
        other_folder = os.path.join(source_folder, "Others")
        os.makedirs(other_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(other_folder, file))
        print(f"Moved: {file} -> Others")

print("\nFile organization completed.")
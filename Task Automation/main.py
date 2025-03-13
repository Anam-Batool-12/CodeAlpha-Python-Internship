import os
import hashlib
import shutil

folder_path = "C:/Users/YourUsername/Documents"
duplicates_folder = os.path.join(folder_path, "Duplicates")
os.makedirs(duplicates_folder, exist_ok=True)
hashes = {}


def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def remove_duplicates():
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if folder_path in file_path and "Duplicates" in file_path:
                continue

            file_hash = get_file_hash(file_path)

            if file_hash in hashes:
                shutil.move(file_path, os.path.join(duplicates_folder, file))
                print(f"Moved duplicate: {file}")
            else:
                hashes[file_hash] = file_path


if __name__ == "__main__":
    remove_duplicates()
    print("Done!")

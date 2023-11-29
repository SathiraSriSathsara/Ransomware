from cryptography.fernet import Fernet
import os

def decrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as thefile:
            contents_encrypted = thefile.read()
        contents_decrypted = Fernet(key).decrypt(contents_encrypted)
        with open(file_path, "wb") as thefile:
            thefile.write(contents_decrypted)
    except (PermissionError, IsADirectoryError):
        print(f"Skipping {file_path} due to lack of permissions or it's a directory.")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def decrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(file_path, key)

if __name__ == "__main__":
    key_file_path = "thekey.key"

    if not os.path.exists(key_file_path):
        print("Key file not found. Make sure the key file is available.")
        exit(1)

    with open(key_file_path, "rb") as key_file:
        key = key_file.read()

    files_and_directories = [f for f in os.listdir() if f not in ["app.py", "thekey.key"]]

    print("Files and Directories Decrypted!!")

    for item in files_and_directories:
        item_path = os.path.join(os.getcwd(), item)
        if os.path.isfile(item_path):
            decrypt_file(item_path, key)
        elif os.path.isdir(item_path):
            decrypt_directory(item_path, key)

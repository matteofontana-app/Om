import bpy
import os
import platform
import subprocess

def open_folder(path):
    # Check if the path exists
    if not os.path.exists(path):
        print(f"Path does not exist: {path}")
        return
    
    # Get the operating system
    system = platform.system()

    # Open folder in Finder (macOS)
    if system == "Darwin":
        subprocess.run(["open", path])
    
    # Open folder in File Explorer (Windows)
    elif system == "Windows":
        subprocess.run(["explorer", path.replace("/", "\\")])
    
    else:
        print(f"Unsupported operating system: {system}")

# Example usage:
# Set your path here
folder_path = openURLVar

# Call the function to open the folder
open_folder(folder_path)

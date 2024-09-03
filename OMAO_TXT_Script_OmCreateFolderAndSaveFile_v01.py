import os

def create_project_folder_structure(root_code, name, root_url, save_blend=False, blend_code=None, subject=None, project_file_name=None, version=None):
    # Construct the root folder name
    root_folder_name = f"{root_code}_{name}"
    root_folder_path = os.path.join(root_url, root_folder_name)
    
    # Check if the root folder already exists
    if os.path.exists(root_folder_path):
        print(f"Error: The root folder '{root_folder_name}' already exists at '{root_url}'. Operation aborted.")
        return
    
    # Define the folder structure
    folder_structure = {
        "_Master": ["00_Client", "10_Internal"],
        "00_Received": ["00_Client", "05_Internal"],
        "05_Production": {
            "00_Render": ["00_Frames", "05_Video"],
            "05_Editing": [],
            "10_Cache": [],
            "15_Data": [],
            "20_Models": [],
            "25_Textures": ["00_Graphics", "05_Materials", "10_SurfaceImperfections", "15_Bokehs"],
            "30_Audio": ["00_SFX", "05_Tracks", "10_Edited"]
        },
        "10_SourceProjects": ["Blender", "Illustrator", "Photoshop"],
        "20_Temp": []
    }

    # Function to create folders recursively
    def create_folders(base_path, structure):
        for folder, subfolders in structure.items():
            folder_path = os.path.join(base_path, folder)
            os.makedirs(folder_path, exist_ok=True)
            if isinstance(subfolders, dict):
                create_folders(folder_path, subfolders)
            elif isinstance(subfolders, list):
                for subfolder in subfolders:
                    subfolder_path = os.path.join(folder_path, subfolder)
                    if not os.path.exists(subfolder_path):
                        os.makedirs(subfolder_path, exist_ok=True)
                    else:
                        print(f"Folder '{subfolder_path}' already exists, skipping creation.")

    # Create the root folder and the structure inside
    create_folders(root_folder_path, folder_structure)
    print(f"Project folder structure created at: {root_folder_path}")
    
    # Save the Blender file if save_blend is True
    if save_blend and blend_code and subject and project_file_name and version is not None:
        blender_folder_path = os.path.join(root_folder_path, "10_SourceProjects", "Blender")
        
        # Ensure the Blender folder exists
        if not os.path.exists(blender_folder_path):
            try:
                os.makedirs(blender_folder_path)
                print(f"Directory created: {blender_folder_path}")
            except Exception as e:
                print(f"Error creating directory {blender_folder_path}: {e}")
                return
        
        # Format the version to always have two digits
        version_str = f"{version:02}"
        
        # Construct the file name
        file_name = f"{blend_code}_BL_{subject}_{project_file_name}_v{version_str}.blend"
        
        # Construct the full path
        full_path = os.path.join(blender_folder_path, file_name)
        
        # Check if the file already exists
        if os.path.exists(full_path):
            print(f"Error: The file '{file_name}' already exists at '{blender_folder_path}'. Operation aborted.")
            return
        
        # Save the blender file
        try:
            bpy.ops.wm.save_as_mainfile(filepath=full_path)
            print(f"Blender file saved as: {full_path}")
        except Exception as e:
            print(f"Error saving Blender file: {e}")

# Example usage
root_code = kindOfProjectVar  # This is the project code used for the root folder
name = nameOfProjectVar
root_url = selectedURLVar
save_blend = saveBlendFileVar  # Boolean variable whether to save the blend file or not
blend_code = blendFileCodeVar  # This is the code used for the Blender file
subject = blendFileSubjectCodeVar
project_file_name = projectFileNameVar
version = verisonNumberVar

create_project_folder_structure(root_code, name, root_url, save_blend, blend_code, subject, project_file_name, version)

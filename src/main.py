# working of basic file opertaions using shutil.
import os
import shutil

# locate all .jpeg files on desktop and store them in file named
directory = '/home/anant/Desktop'

# files = os.listdir(directory)
# for file in files:
#     print(file)
    

##### Search for files with a specific extension function 

def search_files_with_extensions(directory, extensions):
    
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(extensions):
                matching_files.append(os.path.join(root,file))
    
    return matching_files

for file in search_files_with_extensions(directory='/home/anant/Desktop', extensions='.jpeg'):
    print(file)
    

# Function to Store all the files of a specific extension type into a new directory at the specified path.
def create_directory_for_files_with_extensions_to_dest(src, extensions, dest_path):
    
    try:
        # create the directory for the specified path.
        os.mkdir(dest_path)
        print(f"Created directory '{dest_path}'")
    
        # next step is to fetch all the files with the specific extension
        req_files = search_files_with_extensions(src, extensions)
        
        # push the files into dest_path
        for file_path in req_files:
            try:
                # Extract the filename from the file path
                file_name = os.path.basename(file_path)
                # Construct the destination path
                destination_path = os.path.join(dest_path, file_name)
                # move the file to the target directory
                shutil.move(file_path, destination_path)
                print(f"Successfully moved '{file_path}' to '{destination_path}'")
            except Exception as e:
                print(f"Failed to move '{file_path}': {e}")
            
    except FileExistsError:
        print(f"Directory '{dest_path}' already exists")
    except Exception as e:
        print(f"Error creating directory or moving files: {e}")
        
dest = '/home/anant/Desktop/AnimePhotos'
create_directory_for_files_with_extensions_to_dest(directory, extensions='.jpeg', dest_path=dest)
import os
import shutil

#### Function to move all files from a src directory to a destn directory

def move_all_files(src, dest):
    
    # check if src and dest exist or are valid directories
    if not os.path.exists(src):
        print("----ERROR : source directory path that you provided does't exist, please enter a valid path for the source directory.")
    elif not os.path.exists(dest):
        print("----WARNING : destination directory path that you provided does't exist, a new directory at the same path has been created")
        
    else:
        
        for file_name in os.listdir(src):
            src_file = os.path.join(src, dest)
            dest_file = os.path.join(dest, file_name)
            
            if os.path.isfile(src_file):
                
                try:
                    # shutil will itself make new files at dest_file path while creating moving a files
                    shutil.move(src_file,dest_file)
                    # print the confirmation message
                    print(f"Successfully moved '{src_file}' to '{dest_file}'")
                # if an exception occurs
                except Exception as e:
                    print(f"Failed to move '{src_file}' to '{dest_file}': {e}")
                    


# Testing the transfer function.
src_dir = '/home/anant/Desktop/'
dest_dir = '/home/anant/Desktop/AnimePhotos'

move_all_files(src_dir,dest_dir)
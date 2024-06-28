# working of basic file opertaions using shutil.
import os

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

#### simulating the search file function.
for file in search_files_with_extensions(directory='/home/anant/Desktop', extensions='.jpeg'):
    print(file)
    
    

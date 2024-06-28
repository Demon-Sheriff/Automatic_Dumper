import os
dir = '/home/anant/Desktop/Yulu_Project' # example directory

#### Fucntion to list all the files as objects in a given directory.

def list_all_files(directory):
    
    # store all the files in a list
    allFiles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            allFiles.append(os.path.join(root, file))
    
    return allFiles


#### Function to print all file names in a directory.
def print_all_files(directory):
    
    for file in os.listdir(dir):
        print(file)
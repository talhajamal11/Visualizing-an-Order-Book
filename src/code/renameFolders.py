import os

directory = "/Users/talhajamal/Documents/Coding Practice/Python Projects/Visualizing-an-Order-Book/src/data"

# Specify hidden files to be ignored
upper_directory = [f for f in os.listdir(directory) if not f.startswith('.')]

# Function to rename all folders in both level directories
def renameFolders(dir:str) -> None:
    os.chdir(dir)
    folders = [f for f in os.listdir(dir) if not f.startswith('.')]
    for folder in folders:
        os.rename(folder, folder.removeprefix("LOBSTER_SampleFile_"))
    return None

for d in upper_directory:
    renameFolders(directory+"/"+d)
import os

directory = "/Users/talhajamal/Documents/Coding Practice/Python Projects/Visualizing-an-Order-Book/src/data"

# Specify hidden files to be ignored
upper_directory = [f for f in os.listdir(directory) if not f.startswith('.')]

# Function to rename all files in both level directories
def renameFiles(dir:str) -> None:
    os.chdir(dir)
    files = [f for f in os.listdir(dir) if not f.startswith('.')]
    for file in files:
        os.rename(file, file.removeprefix("LOBSTER_SampleFile_"))
    return None

for d in upper_directory:
    renameFiles(directory+"/"+d)
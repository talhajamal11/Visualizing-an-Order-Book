"""
This file downloads order book data and reconstructs the order book for data visualization
"""

# Import relevant modules

import os
from urllib.request import urlretrieve
from zipfile import ZipFile


# Functions to download data, unzip, and delete zipped files
def download_lobster_data(url:str, directory:str, folderList:list) -> None:
    """ 
    Download data
    Sample Link to download file:
    # https://lobsterdata.com/info/sample/LOBSTER_SampleFile_AMZN_2012-06-21_5.zip
    """

    # If Directory is not present, Create Directory
    if os.path.exists(directory) == False:
        print("Creating directory to download and save Lobster Data to")
        os.mkdir(directory)
    else:
        print("Directory for Lobster Data exists")
    
    # Iterate over list of Folder Names
    for folder in folderList:
        # Explicitly Change directory to save files in this location
        os.chdir(directory)
        _zippedFolderPath= directory + str(folder)
        _unzippedFolderPath = _zippedFolderPath.removesuffix(".zip")
        _url = url + str(folder)
        _renamedFolder = folder.removeprefix("LOBSTER_SampleFile_").removesuffix(".zip")

        # If renamed Folders exist, exit loop
        if os.path.exists(_renamedFolder):
            print("Renamed Folder {} already exist...".format(_renamedFolder))
            continue  

        # If Zipped or Unzipped Folders are not present, download zip folders and unzip them
        if (not os.path.exists(_unzippedFolderPath)) and (not os.path.exists(_zippedFolderPath)):
            print("Zipped Folder not present, Downloading Zipped Folder...", _url)
            urlretrieve(_url, filename=folder)
            print("Unzipping Folder: ", folder)
            with ZipFile(_zippedFolderPath, 'r') as zip:
                os.mkdir(_renamedFolder)
                zip.extractall(path=os.path.abspath(_renamedFolder))
            # Delete Zipped Folder after Unzipping
            os.remove(_zippedFolderPath)

        # If Unzipped Folders and Zipped Folders exist, delete zipped folders
        elif (os.path.exists(_zippedFolderPath)) and (os.path.exists(_unzippedFolderPath)):
            os.remove(_zippedFolderPath)

        # If Zipped Folders Exist, Unzip them
        elif (os.path.exists(_zippedFolderPath) and (not os.path.exists(_renamedFolder))):
            print("Zipped Folders present, Unzipping File: ", folder)
            with ZipFile(_zippedFolderPath) as zip:
                os.mkdir(_renamedFolder)
                zip.extractall(path=os.path.abspath(_renamedFolder))
            os.remove(_zippedFolderPath)
        else:
            print("The Unzipped Folder {} already exists".format(_renamedFolder))

    return None


if __name__=='__main__':

    lobster_url = "https://lobsterdata.com/info/sample/"
    lobster_data_path = "/Users/talhajamal/Documents/Coding Practice/Python Projects/Visualizing-an-Order-Book/src/data/lobster/"
    lobster_folders = ["LOBSTER_SampleFile_AMZN_2012-06-21_1.zip", 
                     "LOBSTER_SampleFile_AMZN_2012-06-21_5.zip",
                     "LOBSTER_SampleFile_AMZN_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_AAPL_2012-06-21_1.zip",
                     "LOBSTER_SampleFile_AAPL_2012-06-21_5.zip",
                     "LOBSTER_SampleFile_AAPL_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_GOOG_2012-06-21_1.zip",
                     "LOBSTER_SampleFile_GOOG_2012-06-21_5.zip",
                     "LOBSTER_SampleFile_GOOG_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_INTC_2012-06-21_1.zip",
                     "LOBSTER_SampleFile_INTC_2012-06-21_5.zip",
                     "LOBSTER_SampleFile_INTC_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_1.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_5.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_AAPL_2012-06-21_30.zip",
                     "LOBSTER_SampleFile_AAPL_2012-06-21_50.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_30.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_50.zip",
                     "LOBSTER_SampleFile_SPY_2012-06-21_30.zip",
                     "LOBSTER_SampleFile_SPY_2012-06-21_50.zip"
                     ]

    # Download, Unzip and Delete Zip Files
    download_lobster_data(lobster_url, lobster_data_path, lobster_folders)
    

    
        

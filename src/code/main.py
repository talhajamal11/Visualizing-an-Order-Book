"""
This file downloads order book data and reconstructs the order book for data visualization
"""

# Import relevant modules

import os
import gzip
import shutil
import dload 
import requests
from urllib.request import urlretrieve
from zipfile import ZipFile

import requests, zipfile, io



# Functions to download data

def download_nasdaq_data(directory:str, url:str, filename:str) -> None:
    """ 
    Download data
    """
    if os.path.exists(directory) == False:
        print("Creating directory to download and save Nasdaq Data to")
        os.mkdir(directory)
    else:
        print("Directory for Nasdaq Data exists")
    
    directory = directory + str(filename) + str("/")
    print(directory)

    if os.path.exists(directory) == False:
        print("Download...", url)
        urlretrieve(url, filename)
    else:
        print("The File Exists")

    return None

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
        print("Zipped Path: ", _zippedFolderPath)
        _unzippedFolderPath = _zippedFolderPath.removesuffix(".zip")
        print("Unzipped Path: ", _unzippedFolderPath)
        _url = url + str(folder)
        print(_url)

        # If Unzipped Folders are not present, check if Zipped Folders are present
        if not os.path.exists(_unzippedFolderPath):
            # If Zipped Folders are not present, download Zipped Folders and Unzip them
            if not os.path.exists(_zippedFolderPath):
                print("Zipped Folder not present, Downloading Zipped Folder...", url)
                urlretrieve(_url, filename=folder)
                print("Unzipping Folder: ", folder)
                with ZipFile(_zippedFolderPath, 'r') as zip:
                    os.mkdir(_unzippedFolderPath)
                    zip.extractall(path=_unzippedFolderPath)
            elif os.path.exists(_zippedFolderPath):
                print("Zipped Folders present, Unzipping File: ", folder)
                with ZipFile(_zippedFolderPath) as zip:
                    os.mkdir(_unzippedFolderPath)
                    zip.extractall(path=_unzippedFolderPath)
                
        else:
            print("The Unzipped Folders already exists")

    return None

if __name__=='__main__':

    """
    nasdaq_url = "https://emi.nasdaq.com/ITCH/Nasdaq%20ITCH/"
    nasdaq_file_name = "tvagg.gz"
    nasdaq_data_path = "/Users/talhajamal/Documents/Coding Practice/Python Projects/Visualizing-an-Order-Book/src/data/nasdaq/"

    download_nasdaq_data(nasdaq_data_path, nasdaq_url, nasdaq_file_name)
    """

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
                     "LOBSTER_SampleFile_MSFT_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_10.zip"
                     ]

    download_lobster_data(lobster_url, lobster_data_path, lobster_folders)

    
    

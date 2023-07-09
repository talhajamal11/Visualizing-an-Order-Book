"""
This file downloads order book data and reconstructs the order book for data visualization
"""

# Import relevant modules

import os
import gzip
from urllib.request import urlretrieve



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

def download_lobster_data(directory:str, url:str, folderList:list):
    """ 
    Download data
    """
    if os.path.exists(directory) == False:
        print("Creating directory to download and save Lobster Data to")
        os.mkdir(directory)
    else:
        print("Directory for Lobster Data exists")
    
    for folder in folderList:
        _directory = directory + str(folder) + str("/")
        print(_directory)
        os.chdir(directory)
        if os.path.exists(_directory) == False:
            print("Download...", url)
            urlretrieve(url, folder)
        else:
            print("The Folder Exists")

    return None

# https://lobsterdata.com/info/sample/LOBSTER_SampleFile_AMZN_2012-06-21_5.zip

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
                     "LOBSTER_SampleFile_GOOG_2012-06-21_10.zip"
                     "LOBSTER_SampleFile_INTC_2012-06-21_1.zip",
                     "LOBSTER_SampleFile_INTC_2012-06-21_5.zip",
                     "LOBSTER_SampleFile_INTC_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_1.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_10.zip",
                     "LOBSTER_SampleFile_MSFT_2012-06-21_10.zip"
                     ]
    
    download_lobster_data(lobster_data_path, lobster_url, lobster_folders)

    
    

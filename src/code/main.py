"""
This file downloads order book data and reconstructs the order book for data visualization
"""

# Import relevant modules
from downloadLobsterData import download_lobster_data


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
    

    
        

"""
This file has functions that help read the message file in a dataframe 

"""

#Import Relevant Modules
import os
import pandas as pd


def readMessage(filePath:str) -> pd.DataFrame:
    # Trading starts from 9:30am till 4pm
    # The Time is recorded in seconds post midnight with milliseconds or nanoseconds accuracy 
    _startOfTrading = 9.5*60*60
    _endOfTrading = 16*60*60
    _df = pd.read_csv(filePath,
                      names=["Time", "EventType", "Order ID", "Size", "Price", "Direction"])
    
    # Make sure trading data is between trading times 
    _df = _df[_df["Time"] >= _startOfTrading]
    _df = _df[_df["Time"] <= _endOfTrading]

    # Check for Trading Halts
    _halt = list(_df.index[(_df.EventType == 7) & (_df.Direction == -1)])
    _quote = list(_df.index[(_df.EventType == 7) & (_df.Direction == 0)])
    _resume = list((_df.index[(_df.EventType == 7) & (_df.Direction == 1)]))

    if (len(_halt) == 0) & (len(_quote) == 0) & (len(_resume) == 0):
        print("Trading Halts not detected")
    elif (len(_halt) != 0):
        print("Trading Halts present at the following indexes: ", _halt)
    elif (len(_quote) != 0):
        print("Trading Quotes present at the following indexes: ", _quote)
    elif (len(_resume) != 0):
        print("Trading Resumed at the following indexes: ", _resume)

    return _df

path = "/Users/talhajamal/Documents/Coding Practice/Python Projects/Visualizing-an-Order-Book/src/data/lobster/AAPL_2012-06-21_1/AAPL_2012-06-21_34200000_57600000_message_1.csv"

df = readMessage(path)
print(df)

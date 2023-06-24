# This script is used to parse ITCH data
import pandas as pd

# The parser uses format strings according to the following formats dictionaries:

event_codes = {'O': 'Start of Messages',
               'S': 'Start of System Hours',
               'Q': 'Start of Market Hours',
               'M': 'End of Market Hours',
               'E': 'End of System Hours',
               'C': 'End of Messages'
               }

encoding = {'primary_market_maker': {'Y': 1, 'N': 0},
            'printable'           : {'Y': 1, 'N': 0},
            'buy_sell_indicator'  : {'B': 1, 'S': -1},
            'cross_type'          : {'O': 0, 'C': 1, 'H': 2},
            'imbalance_direction' : {'B': 0, 'S': 1, 'N': 0, 'O': -1}
            }

formats = {
            ('integer', 2): 'H',  # int of length 2 => format string 'H'
            ('integer', 4): 'I',
            ('integer', 6): '6s',  # int of length 6 => parse as string, convert later
            ('integer', 8): 'Q',
            ('alpha',   1): 's',
            ('alpha',   2): '2s',
            ('alpha',   4): '4s',
            ('alpha',   8): '8s',
            ('price_4', 4): 'I',
            ('price_8', 8): 'Q',
        }

messages_path = "/Users/talhajamal/Documents/Coding Practice/Python Projects/Visualizing-an-Order-Book/src/data/message_types.xlsx"

messages_types = pd.read_excel(
    messages_path,
    sheet_name='messages'
).sort_values('id').drop('id', axis=1)

print(messages_types)
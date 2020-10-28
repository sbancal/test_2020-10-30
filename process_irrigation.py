#!/usr/bin/env python3

'''
Process humidity data aquired in the soil of a field of fruit trees

These data are read from a JSON file, converted to a Pandas DataFrame.
They are cleaned (removing saturated values which correspond to "no data")

Finaly we plot it in separated files (one per month) :
+ irrigation_graph_2020-06.png
+ irrigation_graph_2020-07.png
+ irrigation_graph_2020-08.png
'''

import json
import pandas as pd

SOURCE_FILE = 'eco-sensors_irrigation_2020-06-01_2020-08-31.json'


if __name__ == '__main__':
    # Read JSON File
    with open(SOURCE_FILE, 'r') as f:
        data_from_json = json.load(f)

    # Read Labels
    labels = [
        data_from_json[0]['datasets']['label'],
        data_from_json[1]['datasets']['label'],
        data_from_json[2]['datasets']['label'],
    ]

    # Prepare pd.DataFrame object
    humidity_dataframe = pd.DataFrame(
        data={
            labels[0]: data_from_json[0]['datasets']['data'],
            labels[1]: data_from_json[1]['datasets']['data'],
            labels[2]: data_from_json[2]['datasets']['data'],
        },
        index=data_from_json[0]['labels'],
        dtype='float'
    )
    humidity_dataframe.index = pd.to_datetime(humidity_dataframe.index)

    # Print that DataFrame to see what's inside
    print('humidity_dataframe:')
    print(humidity_dataframe, end='\n\n')

    print('humidity_dataframe.index:')
    print(humidity_dataframe.index, end='\n\n')

    print('humidity_dataframe.describe():')
    print(humidity_dataframe.describe(), end='\n\n')

    print('humidity_dataframe.dtypes:')
    print(humidity_dataframe.dtypes, end='\n\n')

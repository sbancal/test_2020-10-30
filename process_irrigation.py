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
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

SOURCE_FILE = 'eco-sensors_irrigation_2020-06-01_2020-08-31.json'


def clean_data(data):
    '''
    Clean data object
    Saturated values (200) are replaced with np.nan
    '''
    data[data == 200] = np.nan


def save_plot_to_file(dataframe,
                      title, labels,
                      start_date, end_date,
                      filename):
    '''
    Will prepare a graph with 3 subplots from the dataframe
    and save it to a file
    '''
    time = dataframe[start_date:end_date].index
    data = [dataframe[start_date:end_date][labels[i]].values for i in range(3)]

    fig = plt.figure(figsize=(10, 10), dpi=100)
    axes = fig.subplots(3, 1, sharex=True)
    axes[0].set_title(title)

    for i in range(3):
        axes[i].plot(time, data[i], label=labels[i])

    fig.autofmt_xdate()
    fig.savefig(filename)


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

    # Clean data
    for label in labels:
        clean_data(humidity_dataframe[label])

    save_plot_to_file(
        humidity_dataframe,
        'Irrigation June 2020', labels,
        '2020-06-01', '2020-06-30',
        'irrigation_graph_2020-06.png'
    )

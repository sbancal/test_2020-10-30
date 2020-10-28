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
import pprint

SOURCE_FILE = 'eco-sensors_irrigation_2020-06-01_2020-08-31.json'

if __name__ == '__main__':
    with open(SOURCE_FILE, 'r') as f:
        data_from_json = json.load(f)

    pprint.pprint(data_from_json)

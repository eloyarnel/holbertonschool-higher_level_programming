#!/usr/bin/env python3
"""
Convert CSV data into JSON format.

Reads a CSV file using DictReader,
converts rows into dictionaries,
and writes the data to data.json.

Returns:
    True if successful
    False if an error occurs
"""


import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        # Open and read the CSV file, converting each row into a dictionary
        with open(csv_filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Write the list of dictionaries as JSON to data.json
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)

        return True
    except FileNotFoundError:
        return False

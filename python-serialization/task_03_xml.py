#!/usr/bin/env python3
"""
XML serialization and deserialization module.

Provides:
- serialize_to_xml(dictionary, filename)
- deserialize_from_xml(filename)
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Create the root <data> element that will contain all dictionary entries
    root = ET.Element("data")

    # Add each key-value pair as a child element under the root
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # XML only stores strings, so convert value

    # Write the XML tree to the file
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    try:
        # Parse the XML file and get the root element
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text

        return dictionary
    except (ET.ParseError, FileNotFoundError):
        return None

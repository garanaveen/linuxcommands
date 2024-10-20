# Every component has xml file and its correponding brs file.
# There can be many nodes in the xml file and every node has an id string to uniquely identify the node.

# This script first collects all the id-string from the xml file and then searches for the same id-string in the brs file.

# If the id-string is not found in the brs file, then it is considered as unused node and needs to be reported as output.

# This script is written in python 3.6.4

# Usage: python findunusednodesinbrs.py <xml_file> <brs_file>

# Example: python findunusednodesinbrs.py test.xml test.brs

import sys
import re

def get_id_strings_from_xml(xml_file):
    id_strings = []
    with open(xml_file, 'r') as f:
        for line in f:
            match = re.search(r'id="([^"]+)"', line)
            if match:
                id_strings.append(match.group(1))
    return id_strings

def search_id_strings_in_brs(id_strings, brs_file):
    unused_nodes = []
    with open(brs_file, 'r') as f:
        brs_content = f.read()
        for id_string in id_strings:
            if id_string not in brs_content:
                unused_nodes.append(id_string)
    return unused_nodes

def main():
    if len(sys.argv) != 3:
        print("Usage: python findunusednodesinbrs.py <xml_file> <brs_file>")
        sys.exit(1)

    xml_file = sys.argv[1]
    brs_file = sys.argv[2]

    id_strings = get_id_strings_from_xml(xml_file)
    unused_nodes = search_id_strings_in_brs(id_strings, brs_file)

    if unused_nodes:
        print("Unused nodes found in brs file:")
        for node in unused_nodes:
            print(node)
    else:
        print("No unused nodes found in brs file")

if __name__ == '__main__':
    main()

# End of script
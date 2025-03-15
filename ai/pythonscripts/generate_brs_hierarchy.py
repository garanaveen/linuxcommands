"""
In brightscript programming, for every component there is xml file and its corresponding brs file.

If there is a brs file without xml file, that means its not a component on its own and needs to be included in another xml file.

The syntax for including a brs file in it's xml file is as follows (CustomComponent is the name of the component).

CustomComponent.xml:
    <script type="text/brightscript" uri="CustomComponent.brs" />
    <script type="text/brightscript" uri="Utils.brs" />

Here CustomComponent.brs is the brs exclusively for CustomComponent and it won't be included in any other xml files.

However, Utils.brs could be more of a general utility and might be included in other xml files.

I want you to write a python script which walks all the directories from the directory it is executed from and finds all the xml files and creates a tree diagram as follows,

CustomComponent.xml
  |
  ____ CustomComponent.brs
  ____ Utils.brs

This isn't an exact format to follow but more of an idea. Use the best possible graphs that is suited for this usecase.
"""

import os
import xml.etree.ElementTree as ET
from anytree import Node, RenderTree
from collections import defaultdict

def find_xml_files(start_dir):
    """Walk through directories and find all XML files."""
    xml_files = []
    for root, _, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".xml"):
                xml_files.append(os.path.join(root, file))
    return xml_files

def parse_xml_for_scripts(xml_file):
    """Parse an XML file and extract the URIs of included .brs files."""
    brs_files = []
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for script in root.findall(".//script"):
            if script.attrib.get("type") == "text/brightscript":
                brs_files.append(script.attrib.get("uri"))
    except ET.ParseError as e:
        print(f"Error parsing {xml_file}: {e}")
    return brs_files

def build_tree(start_dir, inclusion_threshold):
    """Build a tree structure representing XML and .brs file relationships."""
    xml_files = find_xml_files(start_dir)
    brs_inclusion_count = defaultdict(int)
    xml_to_brs_map = {}

    # First pass: Count how many times each .brs file is included
    for xml_file in xml_files:
        brs_files = parse_xml_for_scripts(xml_file)
        xml_to_brs_map[xml_file] = brs_files
        for brs_file in brs_files:
            brs_inclusion_count[brs_file] += 1

    # Second pass: Build the tree, excluding .brs files that exceed the threshold
    root_node = Node("Project Root")
    for xml_file, brs_files in xml_to_brs_map.items():
        xml_node = Node(os.path.basename(xml_file), parent=root_node)
        for brs_file in brs_files:
            if brs_inclusion_count[brs_file] <= inclusion_threshold:
                Node(brs_file, parent=xml_node)

    return root_node

def main():
    import argparse

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Generate a tree diagram of XML and .brs file relationships.")
    parser.add_argument(
        "--inclusion-threshold",
        type=int,
        default=3,
        help="Maximum number of XML files a .brs file can be included in before it is excluded from the hierarchy."
    )
    args = parser.parse_args()

    start_dir = os.getcwd()
    tree_root = build_tree(start_dir, args.inclusion_threshold)

    # Render the tree structure
    for pre, fill, node in RenderTree(tree_root):
        print(f"{pre}{node.name}")

if __name__ == "__main__":
    main()

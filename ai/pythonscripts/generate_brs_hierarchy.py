"""
This script generates a tree diagram of XML and .brs file relationships in a BrightScript project.

Each XML file in a BrightScript project can include one or more `.brs` (BrightScript) files using `<script>` tags.
This script walks through all directories starting from the current directory, identifies all XML files, and builds
a tree structure showing which `.brs` files are included in each XML file.

To reduce noise in the output, the script allows you to specify an "inclusion threshold" via a command-line argument.
If a `.brs` file is included in more XML files than the specified threshold, it will be excluded from the output.

### Features:
- Walks through all directories to find XML files.
- Parses XML files to extract included `.brs` files.
- Builds a tree structure showing the relationships between XML and `.brs` files.
- Excludes `.brs` files that are included in more XML files than the specified threshold.

### Usage:
1. Save this script to a file, e.g., `generate_tree.py`.
2. Run the script from the root directory of your project:
   ```
   python generate_tree.py --inclusion-threshold 3
   ```
   Replace `3` with the desired threshold for excluding `.brs` files.

### Example:
Given the following project structure:
```
/project
    CustomComponent.xml
    CustomComponent.brs
    Utils.brs
    Logger.brs
    AnotherComponent.xml
    AnotherComponent.brs
```

And the following XML file contents:
- `CustomComponent.xml`:
  ```xml
  <script type="text/brightscript" uri="CustomComponent.brs" />
  <script type="text/brightscript" uri="Utils.brs" />
  <script type="text/brightscript" uri="Logger.brs" />
  ```

- `AnotherComponent.xml`:
  ```xml
  <script type="text/brightscript" uri="AnotherComponent.brs" />
  <script type="text/brightscript" uri="Logger.brs" />
  ```

Running the script with `--inclusion-threshold 1` will produce:
```
Project Root
├── CustomComponent.xml
│   ├── CustomComponent.brs
│   └── Utils.brs
├── AnotherComponent.xml
│   └── AnotherComponent.brs
```

Here, `Logger.brs` is excluded because it is included in more than 1 XML file.

### Dependencies:
- Python 3.x
- `anytree` library for rendering the tree structure. Install it using:
  ```
  pip install anytree
  ```

### Command-Line Arguments:
- `--inclusion-threshold`: Maximum number of XML files a `.brs` file can be included in before it is excluded from the hierarchy. Default is `3`.

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
    """
    Build a tree structure representing XML and .brs file relationships.

    Args:
        start_dir (str): The directory to start searching for XML files.
        inclusion_threshold (int): Maximum number of XML files a `.brs` file can be included in
                                   before it is excluded from the hierarchy.

    Returns:
        Node: The root node of the tree structure.
    """
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

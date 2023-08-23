import argparse
import re

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Print lines with Sub or Function declarations from a BrightScript file")
parser.add_argument("file_path", help="Path to the BrightScript file")
parser.add_argument("--optional_string", help="Optional string to match along with Sub/Function", default=None)
args = parser.parse_args()

# Regular expression pattern for matching "Sub" or "Function" as whole words
pattern = re.compile(r"^(.*\s)?(Sub|Function)(\s.*)?$", re.IGNORECASE)

# Read the BrightScript file and print lines with "Sub" or "Function"
with open(args.file_path, "r") as file:
    for line in file:
        line = line.strip()  # Remove leading/trailing whitespace
        if pattern.match(line) and "end " not in line.lower():
            print(line)
        elif args.optional_string and args.optional_string.lower() in line.lower():
            print(line)


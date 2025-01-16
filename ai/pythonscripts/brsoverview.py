import argparse
import re

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Print lines with Sub or Function declarations from a BrightScript file")
parser.add_argument("file_path", help="Path to the BrightScript file")
parser.add_argument("--grep", help="Optional string to match along with Sub/Function", default=None)
args = parser.parse_args()

# Regular expression pattern for matching "Sub" or "Function" as whole words
pattern = re.compile(r"^(.*\s)?(Sub|Function)(\s.*)?$", re.IGNORECASE)

# Split grep based on '|' character and store it in a list of strings named search_strings.
if args.grep:
    search_strings = args.grep.split('|')
    # Print the search_strings
    print(search_strings)


# Read the BrightScript file and print lines with "Sub" or "Function"
with open(args.file_path, "r") as file:
    for line in file:
        originalLine = line
        line = line.strip()  # Remove leading/trailing whitespace
        if pattern.match(line) and "end " not in line.lower():
            print(line)
        # Instead of checking args.grep, check if any of the search_strings are in the line.
        elif args.grep and any(grep.lower() in line.lower() for grep in search_strings):
            print(originalLine)
        elif args.grep and args.grep.lower() in line.lower():
            print(originalLine)


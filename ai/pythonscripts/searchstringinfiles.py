"""
File Search and Grep Script

This script searches for a given regex pattern in files whose names are listed in a specified file. 
The script only searches for these files within the directory from where it is executed.

Usage:
    python script.py --grep <search-string> --file <path-of-file-containing-filenames> [--verbose]

Arguments:
    --grep   : The regex pattern to search for within the files.
    --file   : A file containing the names of files that need to be searched.
    --verbose: (Optional) Enable verbose mode to display progress and file search details.

Example:
    Suppose you have a file `file_list.txt` containing:
        log1.txt
        log2.txt
    And you want to search for occurrences of the word "ERROR" in these files:
    
    Run:
        python script.py --grep "ERROR" --file file_list.txt --verbose
    
    This will output lines matching "ERROR" along with the file name and line number.
"""

import argparse
import re
import sys
import os

def find_file(filename, base_dir, verbose=False):
    """Search for the file within the specified base directory."""
    if verbose:
        print(f"Searching for file: {filename} in {base_dir}")
    for root, _, files in os.walk(base_dir):
        if filename in files:
            found_path = os.path.join(root, filename)
            if verbose:
                print(f"Found file: {found_path}")
            return found_path
    return None

def search_in_file(file_path, pattern, verbose=False):
    """Search for the given regex pattern in the specified file."""
    if verbose:
        print(f"Searching in file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if re.search(pattern, line):
                    print(f"{file_path}:{line_number}:{line.strip()}")
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)

def main():
    """Main function to handle argument parsing and execution."""
    parser = argparse.ArgumentParser(description='Search for a regex pattern in multiple files within the current directory.')
    parser.add_argument('--grep', required=True, help='Regex pattern to search for')
    parser.add_argument('--file', required=True, help='File containing list of filenames to search for')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose mode')
    args = parser.parse_args()
    
    base_dir = os.getcwd()  # Use the current working directory
    
    try:
        with open(args.file, 'r', encoding='utf-8') as file_list:
            filenames = [line.strip() for line in file_list if line.strip()]
    except Exception as e:
        print(f"Error reading file list {args.file}: {e}", file=sys.stderr)
        sys.exit(1)
    
    for filename in filenames:
        file_path = find_file(filename, base_dir, args.verbose)
        if file_path:
            search_in_file(file_path, args.grep, args.verbose)
        else:
            print(f"File not found: {filename}", file=sys.stderr)

if __name__ == '__main__':
    main()


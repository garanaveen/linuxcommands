#!/usr/bin/env python3
import argparse
import re
import os
from pathlib import Path
from collections import namedtuple

# Define a structure to hold function/sub information
FunctionInfo = namedtuple('FunctionInfo', ['name', 'type', 'file_path', 'start_line', 'end_line', 'line_count'])

def find_brs_files(directory):
    """Find all .brs files in the given directory and subdirectories."""
    brs_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.brs'):
                brs_files.append(os.path.join(root, file))
    return brs_files

def analyze_brs_file(file_path):
    """Analyze a single BrightScript file and return function/sub information."""
    functions = []

    # Regular expression patterns
    function_start_pattern = re.compile(r"^\s*(Sub|Function)\s+(\w+)\s*\(", re.IGNORECASE)
    function_end_pattern = re.compile(r"^\s*End\s+(Sub|Function)", re.IGNORECASE)

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

        current_function = None
        line_number = 0

        for i, line in enumerate(lines, 1):
            line_stripped = line.strip()

            # Check for function/sub start
            start_match = function_start_pattern.match(line_stripped)
            if start_match:
                func_type = start_match.group(1)
                func_name = start_match.group(2)
                current_function = {
                    'name': func_name,
                    'type': func_type,
                    'start_line': i,
                    'file_path': file_path
                }

            # Check for function/sub end
            elif function_end_pattern.match(line_stripped) and current_function:
                end_line = i
                line_count = end_line - current_function['start_line'] + 1

                function_info = FunctionInfo(
                    name=current_function['name'],
                    type=current_function['type'],
                    file_path=current_function['file_path'],
                    start_line=current_function['start_line'],
                    end_line=end_line,
                    line_count=line_count
                )

                functions.append(function_info)
                current_function = None

    except Exception as e:
        print(f"Error analyzing file {file_path}: {e}")

    return functions

def main():
    parser = argparse.ArgumentParser(
        description="Analyze BrightScript files to find the longest functions and subroutines"
    )
    parser.add_argument(
        "directory",
        nargs='?',
        default=".",
        help="Directory to search for .brs files (default: current directory)"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=20,
        help="Number of top longest functions to display (default: 20)"
    )
    parser.add_argument(
        "--min-lines",
        type=int,
        default=10,
        help="Minimum number of lines to consider (default: 10)"
    )
    parser.add_argument(
        "--sort-by",
        choices=['lines', 'name', 'file'],
        default='lines',
        help="Sort results by: lines (default), name, or file"
    )

    args = parser.parse_args()

    # Find all .brs files
    print(f"Searching for .brs files in: {os.path.abspath(args.directory)}")
    brs_files = find_brs_files(args.directory)

    if not brs_files:
        print("No .brs files found!")
        return

    print(f"Found {len(brs_files)} .brs files")

    # Analyze all files
    all_functions = []
    for file_path in brs_files:
        functions = analyze_brs_file(file_path)
        all_functions.extend(functions)

    # Filter by minimum lines
    filtered_functions = [f for f in all_functions if f.line_count >= args.min_lines]

    if not filtered_functions:
        print(f"No functions/subs found with at least {args.min_lines} lines!")
        return

    # Sort functions
    if args.sort_by == 'lines':
        filtered_functions.sort(key=lambda x: x.line_count, reverse=True)
    elif args.sort_by == 'name':
        filtered_functions.sort(key=lambda x: x.name.lower())
    elif args.sort_by == 'file':
        filtered_functions.sort(key=lambda x: x.file_path)

    # Display results
    print(f"\nFound {len(filtered_functions)} functions/subs with at least {args.min_lines} lines")
    print(f"Showing top {min(args.top, len(filtered_functions))} results:\n")

    print(f"{'Rank':<5} {'Type':<8} {'Lines':<6} {'Function/Sub Name':<30} {'File':<50} {'Location'}")
    print("-" * 120)

    for i, func in enumerate(filtered_functions[:args.top], 1):
        relative_path = os.path.relpath(func.file_path, args.directory)
        location = f"{func.start_line}-{func.end_line}"

        print(f"{i:<5} {func.type:<8} {func.line_count:<6} {func.name:<30} {relative_path:<50} {location}")

    # Summary statistics
    if filtered_functions:
        avg_lines = sum(f.line_count for f in filtered_functions) / len(filtered_functions)
        max_lines = max(f.line_count for f in filtered_functions)

        print(f"\nSummary:")
        print(f"Total functions/subs analyzed: {len(all_functions)}")
        print(f"Functions/subs with ≥{args.min_lines} lines: {len(filtered_functions)}")
        print(f"Average lines (for functions ≥{args.min_lines} lines): {avg_lines:.1f}")
        print(f"Longest function/sub: {max_lines} lines")

        # Show files with most long functions
        file_counts = {}
        for func in filtered_functions:
            rel_path = os.path.relpath(func.file_path, args.directory)
            file_counts[rel_path] = file_counts.get(rel_path, 0) + 1

        if file_counts:
            print(f"\nFiles with most functions ≥{args.min_lines} lines:")
            sorted_files = sorted(file_counts.items(), key=lambda x: x[1], reverse=True)
            for file_path, count in sorted_files[:5]:
                print(f"  {count:3d} functions: {file_path}")

if __name__ == "__main__":
    main()
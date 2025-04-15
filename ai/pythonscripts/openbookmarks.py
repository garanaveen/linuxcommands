#!/usr/bin/env python3

import webbrowser
import argparse

def open_bookmarks(file_path):
    try:
        # Open the file and read URLs line by line
        with open(file_path, "r") as file:
            for line in file:
                url = line.strip()
                if url:  # Ensure the line is not empty
                    webbrowser.open(url)
        print("All bookmarks have been opened in your default browser.")
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Open bookmarks from a file in your default browser.")
    parser.add_argument("--file", required=True, help="Path to the file containing bookmarks")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the function with the provided file path
    open_bookmarks(args.file)

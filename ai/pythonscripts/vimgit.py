import argparse
import subprocess
import os

""" Usage:
python vimgit.py search_pattern

With alias
vimgit search_pattern

TODO : Move this script to linuxcommands repository.
"""

def main():
    """Open an edited but uncommitted file from a Git repository based on search pattern."""

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Open an edited but uncommitted file from a Git repository")
    parser.add_argument("search_pattern", help="Search pattern for the file name")
    args = parser.parse_args()

    # Run 'git diff --name-only' command
    try:
        diff_output = subprocess.check_output(["git", "diff", "--name-only"])
        diff_files = diff_output.decode().splitlines()
    except subprocess.CalledProcessError:
        print("Error: Unable to retrieve the list of edited files.")
        exit(1)

    # Find files that match the search pattern
    matching_files = [file for file in diff_files if args.search_pattern in file]

    # Display matching files or open a single file with vim
    if len(matching_files) > 1:
        print("Matching edited files:")
        for i, file in enumerate(matching_files, start=1):
            print(f"{i}. {file}")
        print("\nMore than one file matching the search_pattern.\nUse a more specific search pattern or choose one of the files to open.")
    else:
        if len(matching_files) == 1:
            file_to_open = matching_files[0]
            os.system(f"vim {file_to_open}")  # Open the file using vim
        else:
            print("No edited files match the search pattern.")

if __name__ == "__main__":
    main()


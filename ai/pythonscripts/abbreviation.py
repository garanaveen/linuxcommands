import os
import sys
import subprocess

def find_files(base_dir, patterns, maxdepth=5):
    """
    Finds files in the given directory matching the specified patterns using the `find` command.

    :param base_dir: The base directory to search in.
    :param patterns: List of filename patterns to search for (e.g., ["abbreviations", "acronyms"]).
    :param maxdepth: Maximum depth for the `find` command.
    :return: List of file paths matching the patterns.
    """
    files = []
    for pattern in patterns:
        try:
            # Use the `find` command to locate files matching the pattern
            result = subprocess.run(
                ['find', base_dir, '-maxdepth', str(maxdepth), '-type', 'f', '-iname', f'*{pattern}*'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            # Add the found files to the list
            files.extend(result.stdout.strip().split('\n'))
        except Exception as e:
            print(f"An error occurred while running the find command: {e}")
    # Remove empty strings (in case no files were found for a pattern)
    return [file for file in files if file]

def search_abbreviation_in_files(file_paths, shortform):
    """
    Searches for a given shortform in multiple files and prints matching lines.

    :param file_paths: List of file paths to search in.
    :param shortform: Shortform to search for (case insensitive for the first word).
    """
    matches = []
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
            
            for line in lines:
                # Split the line into words
                words = line.split(maxsplit=1)
                if len(words) > 0:
                    # Check if the first word matches the shortform (case insensitive)
                    if words[0].lower() == shortform.lower():
                        matches.append(f"{file_path}: {line.strip()}")
        
        except FileNotFoundError:
            print(f"Warning: File not found at path '{file_path}'")
        except Exception as e:
            print(f"An error occurred while processing '{file_path}': {e}")
    
    if matches:
        print("Matches found:")
        for match in matches:
            print(match)
    else:
        print(f"No matches found for shortform: {shortform}")


# Main script
if __name__ == "__main__":
    # Check if the shortform is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python3 abbreviation.py <shortform>")
        sys.exit(1)

    # Shortform to search for
    shortform = sys.argv[1].strip()

    # Base directory to search in
    base_dir = os.path.expanduser('~')  # Start searching from the user's home directory

    # Patterns to search for
    patterns = ['abbreviations', 'acronyms']

    # Find files matching the patterns
    print("Searching for files...")
    file_paths = find_files(base_dir, patterns)

    # Debug info: Print the files found
    if file_paths:
        print("Files found:")
        for file in file_paths:
            print(f"  - {file}")
    else:
        print(f"No files found matching the patterns: {patterns}")

    # Call the function to search for the shortform in the found files
    search_abbreviation_in_files(file_paths, shortform)

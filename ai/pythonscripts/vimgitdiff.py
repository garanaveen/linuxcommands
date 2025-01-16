
"""
When I do a "git diff" I get the list of files as follows,
--- a/gitrepo/file/path
+++ b/gitrepo/file/path

I need a custom command as follows,

vimg b/gitrepo/file/path

This should open the file with vim.

It shouldn't matter in which directory I am in, in that git repository.
It should first trim the "b/" part from the parameter. Then look if "gitrepo/file/path" is a valid path. If not, it should then try "file/path" and then "path"

When it finds the valid path, it should just open it in vim.

This preferably should be in python script which can then be aliased to "vimg"

search keywords : @git @python @vim

"""


import os
import sys
import subprocess

def find_valid_path(repo_root, file_path):
    # Strip the "b/" prefix if present
    if file_path.startswith("b/"):
        file_path = file_path[2:]

    # Try progressively shorter path segments
    path_segments = file_path.split("/")
    for i in range(len(path_segments)):
        # Construct the path by removing leading segments
        path_to_try = os.path.join(repo_root, *path_segments[i:])
        if os.path.isfile(path_to_try):
            return path_to_try
    
    # Return None if no valid path is found
    return None

def main():
    # Check if file path argument is provided
    if len(sys.argv) < 2:
        print("Usage: vimg <file-path>")
        sys.exit(1)
    
    # Get the file path from command line
    file_path = sys.argv[1]
    
    # Get the repository root directory
    try:
        repo_root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
    except subprocess.CalledProcessError:
        print("Not inside a Git repository.")
        sys.exit(1)
    
    # Find the valid path
    valid_path = find_valid_path(repo_root, file_path)
    
    if valid_path:
        # Open the file in vim
        subprocess.call(["vim", valid_path])
    else:
        print("File not found in repository.")

if __name__ == "__main__":
    main()


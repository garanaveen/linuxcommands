"""
Script to generate a GitHub/GitLab link for a specific file in a Git repository.

This script:
1. Determines the repository URL.
2. Identifies the current branch of the repository.
3. Calculates the relative path of the specified file from the repository root.
4. Constructs a link to the file on GitHub/GitLab.
5. Opens the generated link in the default browser.

Typical Usage:
--------------
1. Generate a link for a file and open it in the browser:
   $ python3 generate_file_link.py filename.txt

2. Example Output:
   File Link: https://github.com/username/repo/blob/main/path/to/filename.txt
   (The link will also open in the default browser.)

Requirements:
-------------
- The script must be run inside a Git repository.
- The file must exist within the repository.

Supported Platforms:
--------------------
- Linux
- macOS
- Windows
"""

import subprocess
import os
import sys
import webbrowser

def get_repo_url():
    try:
        # Run the `git remote get-url origin` command to get the repository URL
        result = subprocess.run(['git', 'remote', 'get-url', 'origin'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("Error: Unable to run 'git remote get-url origin'. Make sure you are in a Git repository.")
            print(result.stderr)
            return None

        # Get the repository URL
        repo_url = result.stdout.strip()

        # Convert SSH URL to HTTPS URL if necessary
        if repo_url.startswith("git@"):
            # SSH URL (e.g., git@gitlab.com:username/repo.git)
            repo_url = repo_url.replace(":", "/").replace("git@", "https://")
        elif repo_url.startswith("https://"):
            # HTTPS URL (e.g., https://gitlab.com/username/repo.git)
            pass
        else:
            print("Error: Unsupported URL format.")
            return None

        # Remove `.git` suffix if present
        if repo_url.endswith(".git"):
            repo_url = repo_url[:-4]

        return repo_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_repo_root():
    try:
        # Run the `git rev-parse --show-toplevel` command to get the root directory of the repository
        result = subprocess.run(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("Error: Unable to determine the root of the repository. Make sure you are in a Git repository.")
            print(result.stderr)
            return None

        return result.stdout.strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_current_branch():
    try:
        # Run the `git rev-parse --abbrev-ref HEAD` command to get the current branch name
        result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            print("Error: Unable to determine the current branch. Make sure you are in a Git repository.")
            print(result.stderr)
            return None

        return result.stdout.strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def generate_file_link(filename):
    # Get the repository URL
    repo_url = get_repo_url()
    if not repo_url:
        return None

    # Get the root directory of the repository
    repo_root = get_repo_root()
    if not repo_root:
        return None

    # Get the current branch name
    branch_name = get_current_branch()
    if not branch_name:
        return None

    # Get the absolute path of the file
    file_path = os.path.abspath(filename)

    # Ensure the file is inside the repository
    if not file_path.startswith(repo_root):
        print("Error: The specified file is not inside the repository.")
        return None

    # Get the relative path of the file from the repository root
    relative_path = os.path.relpath(file_path, repo_root)

    # Construct the file link using the current branch name
    file_link = f"{repo_url}/blob/{branch_name}/{relative_path}"
    return file_link

def open_link_in_browser(link):
    try:
        # Use Python's webbrowser module to open the link in the default browser
        webbrowser.open(link)
    except Exception as e:
        print(f"Error: Unable to open the link in the browser. {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate_file_link.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    file_link = generate_file_link(filename)
    if file_link:
        print(f"File Link: {file_link}")
        open_link_in_browser(file_link)
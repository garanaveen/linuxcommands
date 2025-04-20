import subprocess
import os

# Define the tags to search for and their order
tags = ["@urgent", "@todo", "@track"]

def get_journals_in_current_directory():
    """Retrieve the list of journals and filter those in the current directory."""
    try:
        # Execute the jrnl command to list journals
        result = subprocess.run(
            ["jrnl", "--list"],
            capture_output=True,
            text=True,
            check=True
        )
        journals = {}
        current_directory = os.getcwd()
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if "->" in line:
                # Parse journal name and file path
                parts = line.split("->")
                journal_name = parts[0].strip().lstrip("*").strip()
                journal_path = os.path.expandvars(parts[1].strip())
                # Include only journals within the current directory
                if journal_path.startswith(current_directory):
                    journals[journal_name] = journal_path
        return journals
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving journals: {e}")
        return {}

def search_tag(journal_name, tag):
    """Search for entries with a specific tag in a journal."""
    try:
        # Execute the jrnl command to search for the tag
        result = subprocess.run(
            ["jrnl", journal_name, tag, "--short"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error searching for {tag} in {journal_name}: {e}")
        return ""

def main():
    # Get the list of journals in the current directory
    journals = get_journals_in_current_directory()
    if not journals:
        print("No journals found in the current directory.")
        return

    # Dictionary to store results for each tag
    results = {tag: [] for tag in tags}

    # Iterate through each journal and search for each tag
    for journal_name in journals.keys():
        for tag in tags:
            entries = search_tag(journal_name, tag)
            if entries:
                results[tag].append(f"--- Entries from {journal_name} ---\n{entries}")

    # Print the results organized by tag
    for tag in tags:
        print(f"\n### {tag.upper()} ENTRIES ###")
        if results[tag]:
            print("\n".join(results[tag]))
        else:
            print(f"No entries found for {tag}.")

if __name__ == "__main__":
    main()

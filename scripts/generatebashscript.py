import os

#Run this script from your home directory as follows,
#python linuxcommands/scripts/generatebashscript.py
#This generates sourcing_script.sh in the directory where this script is ran from.
#Include this in your .bashrc file.

def search_files(patterns, directory, min_depth, max_depth):
    matches = []
    if max_depth < min_depth:
        return matches

    for root, dirs, files in os.walk(directory):
        current_depth = root.count(os.sep) - directory.count(os.sep)
        if current_depth < min_depth or current_depth > max_depth:
            continue

        # Skip processing symbolic link directories
        if os.path.islink(root):
            continue
        #Skip processing hidden directories
        if root.startswith('.'):
            continue

        if isMacDirectory(root):
            continue

        for file in files:
            file_path = os.path.join(root, file)
            # print("file:", file_path)
            file_name, file_extension = os.path.splitext(file)
            if file_extension == '' and not file_name.startswith('.'):
                for pattern in patterns:
                    if pattern in file_name:
                        matches.append(file_path)
                        print("Bash script generated successfully!", file_path)
                        break

    return matches

def generate_bash_script(file_paths):
    script = "#!/bin/bash\n\n"
    script += "#Run source sourcing_script.sh\n"
    for file_path in file_paths:
        script += "source {}\n".format(file_path)
    return script

def isMacDirectory(root) -> bool:
    return root.endswith("Applications") or \
        root.endswith("Desktop") or \
        root.endswith("Development") or \
        root.endswith("Documents") or \
        root.endswith("Downloads") or \
        root.endswith("Library") or \
        root.endswith("Movies") or \
        root.endswith("Music") or \
        root.endswith("OneDrive - Roku Inc") or \
        root.endswith("Perforce") or \
        root.endswith("Pictures") or \
        root.endswith("Postman") or \
        root.endswith("Public") or \
        root.endswith("archive") or \
        root.endswith("nobuildfirmware") or \
        root.endswith("tmp") or \
        root.endswith("wdmycloud")


# List of patterns to search for
patterns = ["aliases", "bashrc", ".bashrc"]

# Directory to start searching from
directory = os.getcwd()

# Minimum and maximum depth for searching files
min_depth = 0
max_depth = 3

# Search for matching files
matched_files = search_files(patterns, directory, min_depth, max_depth)
print("matched_files created!")

# Generate bash script
bash_script = generate_bash_script(matched_files)
print("bash_script generated!")

# Write the bash script to a file
with open("sourcing_script.sh", "w") as file:
    file.write(bash_script)

print("Bash script generated successfully!")


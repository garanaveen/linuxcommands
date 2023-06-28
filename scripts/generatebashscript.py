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

        for file in files:
            file_path = os.path.join(root, file)
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
    for file_path in file_paths:
        script += "source {}\n".format(file_path)
    return script

# List of patterns to search for
patterns = ["aliases", "bashrc", "pattern3"]

# Directory to start searching from
directory = os.getcwd()

# Minimum and maximum depth for searching files
min_depth = 1
max_depth = 4

# Search for matching files
matched_files = search_files(patterns, directory, min_depth, max_depth)

# Generate bash script
bash_script = generate_bash_script(matched_files)

# Write the bash script to a file
with open("sourcing_script.sh", "w") as file:
    file.write(bash_script)

print("Bash script generated successfully!")


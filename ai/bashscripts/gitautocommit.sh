#!/bin/bash

# Get today's date
current_time=$(date +'%Y-%m-%d_%H:%M')

# Get the hostname
hostname=$(hostname)

# Create the commit message
commit_message="Auto commit - Date: $current_time, Host: $hostname"

# Show the changes that would be committed
git status

# Ask for confirmation
read -p "Do you want to proceed with the commit? (y/n): " confirm

if [ "$confirm" == "y" ]; then
    # Run the git commit command
    git commit -a -m "$commit_message"
    echo "Commit successful!"
else
    echo "Commit aborted."
fi


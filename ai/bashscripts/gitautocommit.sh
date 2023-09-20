#!/bin/bash

# Get today's date
current_date=$(date +'%Y-%m-%d')

# Get the hostname
hostname=$(hostname)

# Create the commit message
commit_message="Auto commit - Date: $current_date, Host: $hostname"

# Run the git commit command
git commit -m "$commit_message"


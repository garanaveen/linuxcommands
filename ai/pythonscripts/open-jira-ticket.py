import sys
import os
import re
import webbrowser

# Base URL for Jira tickets
JIRA_BASE_URL = "https://roku.atlassian.net/browse/"

def open_jira_ticket(ticket_number):
    """Open the Jira ticket in the default web browser."""
    url = f"{JIRA_BASE_URL}{ticket_number}"
    print(f"Opening Jira ticket: {url}")
    webbrowser.open(url)

def find_ticket_in_path(path):
    """Search for a Jira ticket number in the given path."""
    # Regex pattern to match Jira ticket numbers (e.g., ASPEN-1001, AUTO-38095)
    pattern = r"[A-Z]+-\d+"
    match = re.search(pattern, path)
    if match:
        return match.group(0)
    return None

def main():
    # Check if a ticket number is provided as a command-line argument
    if len(sys.argv) > 1:
        ticket_number = sys.argv[1]
    else:
        # If no argument is provided, search for a ticket number in the current path
        current_path = os.getcwd()
        ticket_number = find_ticket_in_path(current_path)
        if not ticket_number:
            print("No Jira ticket number found in the current path.")
            sys.exit(1)

    # Open the Jira ticket
    open_jira_ticket(ticket_number)

if __name__ == "__main__":
    main()

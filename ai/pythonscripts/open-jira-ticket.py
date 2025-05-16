import sys
import os
import re
import webbrowser

def get_jira_base_url():
    """
    Retrieve the Jira base URL from the environment variable.

    Returns:
        str: The Jira base URL.

    Raises:
        SystemExit: If the environment variable is not defined or invalid.
    """
    jira_base_url = os.getenv("JIRA_BASE_URL")
    if not jira_base_url:
        print("Error: The environment variable 'JIRA_BASE_URL' is not defined.")
        sys.exit(1)
    if not jira_base_url.startswith("http"):
        print("Error: The environment variable 'JIRA_BASE_URL' must be a valid URL.")
        sys.exit(1)
    return jira_base_url

def open_jira_ticket(ticket_number, jira_base_url):
    """
    Open the Jira ticket in the default web browser.

    Args:
        ticket_number (str): The Jira ticket number (e.g., AUTO-13263).
        jira_base_url (str): The base URL for Jira tickets.
    """
    url = f"{jira_base_url}/{ticket_number}"
    print(f"Opening Jira ticket: {url}")
    webbrowser.open(url)

def find_ticket_in_path(path):
    """
    Search for a Jira ticket number in the given path.

    Args:
        path (str): The file path to search for a Jira ticket number.

    Returns:
        str or None: The Jira ticket number if found, otherwise None.
    """
    # Regex pattern to match Jira ticket numbers (e.g., ASPEN-1001, AUTO-38095)
    pattern = r"[A-Z]+-\d+"
    match = re.search(pattern, path)
    if match:
        return match.group(0)
    return None

def get_ticket_from_git_branch():
    """
    Retrieve the Jira ticket number from the current Git branch name.

    Returns:
        str or None: The Jira ticket number if found, otherwise None.
    """
    try:
        # Get the current Git branch name
        with os.popen('git rev-parse --abbrev-ref HEAD') as branch:
            branch_name = branch.read().strip()
        # Regex pattern to match Jira ticket numbers (e.g., ASPEN-1001, AUTO-38095)
        pattern = r"[A-Z]+-\d+"
        match = re.search(pattern, branch_name)
        if match:
            return match.group(0)
    except Exception as e:
        print(f"Error retrieving Git branch: {e}")
    return None

def main():
    """
    Main function to handle command-line arguments and open the Jira ticket.

    Usage:
        1. Provide a Jira ticket number as a command-line argument:
           $ python openjiraticket.py AUTO-13263
           This will open the Jira ticket URL: <JIRA_BASE_URL>/AUTO-13263

        2. Run the script without arguments:
           $ python openjiraticket.py
           If the script is run from a directory path containing a Jira ticket number,
           such as "/home/user/projects/AUTO-38606_UpdateFirmwareGitlabJob",
           it will extract the ticket number (e.g., AUTO-38606) and open the corresponding
           Jira ticket URL: <JIRA_BASE_URL>/AUTO-38606

        3. Extract the Jira ticket number from the current Git branch name:
           If the script is run in a Git repository and the branch name contains a Jira ticket number
           (e.g., feature/AUTO-12345), it will extract the ticket number (e.g., AUTO-12345) and open
           the corresponding Jira ticket URL: <JIRA_BASE_URL>/AUTO-12345

        Notes:
        - If no ticket number is found in the current path and no argument is provided,
          the script will exit with an error message.
        - The environment variable 'JIRA_BASE_URL' must be defined and valid.
    """
    # Retrieve and validate the Jira base URL from the environment variable
    jira_base_url = get_jira_base_url()

    # Check if a ticket number is provided as a command-line argument
    if len(sys.argv) > 1:
        ticket_number = sys.argv[1]
    else:
        # If no argument is provided, search for a ticket number in the current path
        current_path = os.getcwd()
        ticket_number = find_ticket_in_path(current_path)
        if not ticket_number:
            # If no ticket number is found in the path, search in the Git branch name
            ticket_number = get_ticket_from_git_branch()
        if not ticket_number:
            print("No Jira ticket number found in the current path or Git branch.")
            sys.exit(1)

    # Open the Jira ticket
    open_jira_ticket(ticket_number, jira_base_url)

if __name__ == "__main__":
    main()

import os
import subprocess

def get_recent_jrnl_command():
    """
    Retrieves the most recent 'jrnl' command from the shell history file.

    Returns:
        str: The most recent 'jrnl' command, or None if no such command is found.
    """
    # Get the shell history file path (default is ~/.bash_history for bash)
    history_file = os.path.expanduser("~/.bash_history")  # Adjust for your shell (e.g., ~/.zsh_history for zsh)
    
    try:
        # Open and read the history file
        with open(history_file, "r") as file:
            commands = file.readlines()
            # Reverse the list to search from the most recent command
            for command in reversed(commands):
                command = command.strip()  # Remove any leading/trailing whitespace
                if command.startswith("jrnl "):  # Check if the command starts with 'jrnl'
                    return command  # Return the most recent 'jrnl' command
        print("No 'jrnl' command found in history.")
        return None
    except FileNotFoundError:
        print("Shell history file not found. Ensure your history is being saved.")
        return None

def extract_journal_name(command):
    """
    Extracts the journal name from a 'jrnl' command.

    Args:
        command (str): The 'jrnl' command string.

    Returns:
        str: The journal name (second word in the command), or None if invalid.
    """
    # Split the command into parts (e.g., "jrnl financial Opened amex credit card")
    parts = command.split()
    if len(parts) >= 2 and parts[0] == "jrnl":  # Ensure the command is valid
        return parts[1]  # Return the journal name (second word)
    return None

def main():
    """
    Main function to find the most recent 'jrnl' command, extract the journal name,
    and execute the corresponding 'jrnl <journal_name> --edit' command.
    """
    # Step 1: Get the most recent 'jrnl' command from history
    recent_jrnl_command = get_recent_jrnl_command()
    if not recent_jrnl_command:
        return  # Exit if no 'jrnl' command is found
    
    # Step 2: Extract the journal name from the command
    journal_name = extract_journal_name(recent_jrnl_command)
    if not journal_name:
        print("Most recent 'jrnl' command is not valid.")
        return  # Exit if the command is invalid
    
    # Step 3: Construct the 'jrnl <journal_name> --edit' command
    edit_command = f"jrnl {journal_name} --edit"
    print(f"Executing: {edit_command}")
    
    # Step 4: Execute the constructed command
    subprocess.run(edit_command, shell=True)

if __name__ == "__main__":
    """
    Entry point of the script. Executes the main function.
    """
    main()

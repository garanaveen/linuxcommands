import os
import subprocess

#todo: Ignore lines in $HOME/.syncrepos that start with '#' character

def check_unstaged_changes(repo_path):
    os.chdir(repo_path)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout.strip():
        return True
    return False

def check_incoming_changes(repo_path, remote_name, branch_name):
    os.chdir(repo_path)
    subprocess.run(["git", "fetch", remote_name])
    result = subprocess.run(["git", "log", f"{branch_name}..{remote_name}/{branch_name}", "--oneline"], capture_output=True, text=True)
    return result.stdout.strip()

def check_outgoing_changes(repo_path, remote_name, branch_name):
    os.chdir(repo_path)
    subprocess.run(["git", "fetch", remote_name])
    result = subprocess.run(["git", "log", f"{remote_name}/{branch_name}..{branch_name}", "--oneline"], capture_output=True, text=True)
    return result.stdout.strip()

def sync_repositories(repositories):
    for repo_info in repositories:
        repo_path, remote_name, branch_name = repo_info
        repo_path = os.path.expanduser(repo_path)

        print(f"Checking repository: {repo_path}")

        if check_unstaged_changes(repo_path):
            print(f"unstaged/uncommitted changes found in ****{repo_path}****")
            return

        incoming_changes = check_incoming_changes(repo_path, remote_name, branch_name)
        if incoming_changes:
            print(f"Incoming changes detected in ****{repo_path}****")
            print(incoming_changes)

        outgoing_changes = check_outgoing_changes(repo_path, remote_name, branch_name)
        if outgoing_changes:
            print(f"Outgoing changes detected: in ****{repo_path}****")
            print(outgoing_changes)

        print("Repository is in sync.\n")

def read_repository_file(file_path):
    repositories = []
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore comments
                    parts = line.split(',')
                    if len(parts) == 3:
                        repositories.append(parts)
    return repositories

if __name__ == "__main__":
    home_directory = os.path.expanduser("~")
    repos_file = os.path.join(home_directory, ".syncrepos")
    additional_repositories = read_repository_file(repos_file)

    # Define the initial repositories in .syncrepos format
    repositories = [
        ("~/git/garanaveen/personal","origin","master"),
        # Add more repositories as needed
    ]

    # Add repositories from the file
    repositories.extend(additional_repositories)

    sync_repositories(repositories)


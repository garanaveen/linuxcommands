import os
import subprocess

def check_unstaged_changes(repo_path):
    os.chdir(repo_path)
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if result.stdout.strip():
        return True
    return False

def check_incoming_changes(repo_path, remote_name, branch_name):
    os.chdir(repo_path)
    subprocess.run(["git", "fetch", remote_name])
    result = subprocess.run(["git", "log", f"{remote_name}/{branch_name}..{branch_name}", "--oneline"], capture_output=True, text=True)
    return result.stdout.strip()

def check_outgoing_changes(repo_path, remote_name, branch_name):
    os.chdir(repo_path)
    subprocess.run(["git", "fetch", remote_name])
    result = subprocess.run(["git", "log", f"{branch_name}..{remote_name}/{branch_name}", "--oneline"], capture_output=True, text=True)
    return result.stdout.strip()

def sync_repositories(repositories):
    for repo_info in repositories:
        repo_path, remote_info = repo_info
        repo_name, branch_name = remote_info.split(',')
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()

        print(f"Checking repository: {repo_path}")
        
        if check_unstaged_changes(repo_path):
            print("Repository has unstaged/uncommitted changes. Sync stopped.")
            return

        incoming_changes = check_incoming_changes(repo_path, repo_name, branch_name)
        if incoming_changes:
            print("Incoming changes detected:")
            print(incoming_changes)
            print("Sync stopped.")
            return

        outgoing_changes = check_outgoing_changes(repo_path, repo_name, branch_name)
        if outgoing_changes:
            print("Outgoing changes detected:")
            print(outgoing_changes)
        
        print("Repository is in sync.\n")

if __name__ == "__main__":
    repositories = [
        ("/home/ngara/ngara-utils/", "origin,master"),
        ("/home/ngara/git/garanaveen/linuxcommands/", "origin,master"),
        ("/home/ngara/ngara-notes/", "origin,master"),
        ("/home/ngara/git/garanaveen/personal", "origin,master"),
        # Add more repositories as needed
    ]
    
    sync_repositories(repositories)


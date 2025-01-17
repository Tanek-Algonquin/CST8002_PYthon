from git import Repo

#Define the path to local repository
repo_path = r"C:\PythonProjects" #raw string to avoid \ new line iseue

#Initialize the repository
repo = Repo(repo_path)

#Check for uncommited changes or uncommited files
if repo.is_dirty() or repo.untracked_files:
    #Stage all changes
    repo.git.add(A=True)
    
    #Commit the changes
    commit_message = "Automated commit from Thonny"
    repo.index.commit(commit_message)
    
    # Print files that were modified or added in the commit
    print(f"Committed changes with message: {commit_message}")
    
    # Print files that were modified or added in the commit
    print("Files that were committed:")
    for diff in repo.head.commit.diff("HEAD~1"):  # Compare with the previous commit
        print(f"- {diff.a_path} (change type: {diff.change_type})")
    
    #Push the changes
    try:
        print("Attempting to pus to remote repository..." )
        repo.remotes.origin.push()
        print("Push Sucessful! :) ")
    except Exception as e:
        print(f"Error pushing changes: {e}")
            
else:
    print("No changes to commit.")
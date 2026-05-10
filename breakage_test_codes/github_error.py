"""
ARCHITECT'S GIT & GITHUB FAILURE DICTIONARY
Logic: Documentation of 'Bridge Failures' between local and remote environments.
"""

# =================================================================
# 01. THE PROTOCOL MISMATCH (The Bracket Trap)
# =================================================================
# ERROR: fatal: protocol '[https' is not supported
# WHY: Including brackets [] or quotes in the URL command.
# BREAK: git remote add origin [https://github.com/user/repo.git]

# FIX: Remove all brackets and symbols. Use the raw URL.
# COMMAND: git remote add origin https://github.com/user/repo.git


# =================================================================
# 02. THE IDENTITY CRISIS (Branch Mismatch)
# =================================================================
# ERROR: error: src refspec main does not match any
# WHY: Trying to push to 'main' when your local branch is still named 'master'.
# BREAK: git push origin main (while on master branch)

# FIX: Rename the local branch to match the remote.
# COMMAND: git branch -M main


# =================================================================
# 03. THE GHOST REPOSITORY (The Typo Error)
# =================================================================
# ERROR: remote: Repository not found / fatal: repository ... not found
# WHY: A spelling mistake in the URL (e.g., 'Joureny' instead of 'Journey').
# BREAK: git remote add origin https://github.com/user/Mispelled_Repo.git

# FIX: Remove the bad origin and add the correctly spelled one.
# COMMAND: 
# git remote remove origin
# git remote add origin https://github.com/user/Correct_Repo.git


# =================================================================
# 04. THE UPSTREAM LOCK (Missing Link)
# =================================================================
# ERROR: fatal: The current branch main has no upstream branch.
# WHY: Local branch is not "linked" to the GitHub branch yet.
# BREAK: git push (on a brand new repo)

# FIX: Use the -u flag to create a permanent tracking link.
# COMMAND: git push -u origin main


# =================================================================
# 05. THE "ALREADY EXISTS" BLOCK
# =================================================================
# ERROR: error: remote origin already exists.
# WHY: You tried to 'add origin' when one is already saved in config.
# BREAK: Running 'git remote add origin ...' twice.

# FIX: Update the existing URL instead of trying to add a new one.
# COMMAND: git remote set-url origin https://github.com/user/repo.git


# =================================================================
# 06. THE AUTHENTICATION BARRIER (Future Error)
# =================================================================
# ERROR: fatal: Authentication failed / Support for password authentication was removed
# WHY: GitHub requires a Personal Access Token (PAT) or SSH, not your password.
# BREAK: Entering your standard login password in the terminal.

# FIX: Generate a Token in GitHub Settings -> Developer Settings -> Tokens.
# Use that Token as your password.


# =================================================================
# 07. THE REJECTED PUSH (Non-Fast-Forward)
# =================================================================
# ERROR: error: failed to push some refs / updates were rejected
# WHY: Someone (or you) changed files on GitHub directly, and your local is now "behind."
# BREAK: Adding a README on GitHub.com and then trying to push from VS Code.

# FIX: Pull the changes from GitHub first, merge them, then push.
# COMMAND: git pull origin main
"""
PHASE 8: THE LOGIC OF SOURCE CONTROL
Philosophy: "Understand the blueprint before you lay the brick."
"""

# =================================================================
# 1. FOUNDATION: FIRST-TIME REPOSITORY SETUP
# =================================================================

# 1.1 Start the engine: Tell your computer to track changes in this folder.
# WHY: Without this, Git is "blind" to your files.
# COMMAND:
# git init

# 1.2 Gather the materials: Put all your files into the "Staging Area."
# WHY: This creates a snapshot of what you want to save.
# COMMAND:
# git add .

# 1.3 Seal the box: Give this snapshot a name and a description.
# WHY: You are creating a permanent "Version" in your history.
# COMMAND:
# git commit -m "Initial Blueprint: Setting up the Architect's Journey"

# 1.4 Define the path: Name your local branch 'main'.
# WHY: Modern GitHub repositories use 'main' as the default standard.
# COMMAND:
# git branch -M main

# 1.5 Set the destination: Link your local folder to your online GitHub URL.
# WHY: Your computer needs to know where the cloud repository is located.
# COMMAND:
# git remote add origin https://github.com/FazalAbbas0/Architect_Journey.git

# 1.6 Launch the payload: Send your code to GitHub and set a permanent link.
# WHY: The '-u' flag (upstream) remembers the link so you don't have to type it again.
# COMMAND:
# git push -u origin main


# =================================================================
# 2. THE DAILY FLOW: POST-MODIFICATION UPDATES
# =================================================================

# 2.1 Select the change: Prepare the specific file for upload.
# WHY: Good artisanship means only saving what is finished and tested.
# COMMAND:
# git add <file_name.py>

# 2.2 Document the work: Write a message explaining what you changed or fixed.
# WHY: This helps you (and others) trace your learning progress later.
# COMMAND:
# git commit -m "Fix: Resolved [Error Name] in Phase X"


# FIX: Pull the changes from GitHub first, merge them, then push.
# COMMAND: git pull origin main

# 2.3 Sync with the cloud: Upload your new commit to GitHub.
# WHY: To ensure your online backup is identical to your local work.
# COMMAND:
# git push
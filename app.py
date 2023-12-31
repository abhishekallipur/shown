import os
from random import randint, choice
from datetime import datetime, timedelta

# Total commits, you can adjust the range if necessary
total_commits = randint(20, 60)

# Track the number of commits made
commit_count = 0

# Start from January 1st, 2024
current_date = datetime(2024, 1, 1)

# List to store commit days
commit_days = []

# Randomly select commit days with skipping 2-3 days in between
while commit_count < total_commits and current_date <= datetime(2024, 2, 29):
    commit_days.append(current_date)

    # Skip 2-3 days (randomly)
    current_date += timedelta(days=randint(2, 3))
    
    commit_count += 1

# Iterate through the selected commit days and simulate commits
for commit_date in commit_days:
    # Random number of commits for the selected day (between 1 and 3 commits)
    for _ in range(randint(1, 3)):
        # Format the commit message and date
        commit_date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Write to file.txt (simulating some change on each commit)
        with open('file.txt', 'a') as f:
            f.write(f"Commit on {commit_date_str}\n")
        
        # Commit with the generated commit date
        os.system(f'git add .')
        os.system(f'git commit --date="{commit_date_str}" -m "Commit on {commit_date_str}"')

# Push to the remote repository
os.system('git push -u origin main')

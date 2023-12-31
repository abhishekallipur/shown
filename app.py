import os
from random import randint
from datetime import datetime, timedelta

# Total number of commits (randomly between 20 and 60)
total_commits = randint(20, 60)

# Track the number of commits made
commit_count = 0

# Start from January 1st, 2024
current_date = datetime(2024, 1, 1)

# Randomly select commit days with skipping 2-3 days in between
while commit_count < total_commits:
    # Create a commit message with the current date
    commit_date_str = current_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Write to file.txt (simulating some change on each commit)
    with open('file.txt', 'a') as f:
        f.write(f"Commit on {commit_date_str}\n")
    
    # Commit with the generated commit date
    os.system(f'git add .')
    os.system(f'git commit --date="{commit_date_str}" -m "Commit on {commit_date_str}"')

    # Increment the commit count
    commit_count += 1

    # Skip 2-3 days (randomly)
    current_date += timedelta(days=randint(2, 3))

# Push to the remote repository
os.system('git push -u origin main')

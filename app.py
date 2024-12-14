import os
from random import randint, choice

# Number of commits you want
total_commits = 60

# Track the number of commits made
commit_count = 0

# List of days from 1 to 365
days = list(range(1, 366))

# Randomly select 60 days to commit on
random_days = sorted([choice(days) for _ in range(total_commits)])

for i in random_days:
    # Skip to next if we already reached 60 commits
    if commit_count >= total_commits:
        break
    
    # Random number of commits for the selected day (between 1 and 10)
    for j in range(randint(1, 10)):
        # Create the commit message with the selected day
        d = str(i) + " days ago"
        
        # Write to file.txt
        with open('file.txt', 'a') as f:
            f.write(d + '\n')
        
        # Commit and push the changes
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')
        
        commit_count += 1
        if commit_count >= total_commits:
            break

# Push to the remote repository
os.system('git push -u origin main')

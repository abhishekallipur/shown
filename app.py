import os
from random import randint, choice
import datetime

# Total number of commits: generate a random number between 20 and 60
total_commits = randint(20, 60)

# Track the number of commits made
commit_count = 0

# Start from day 1 (January 2024)
current_day = 1

# List to store commit days
commit_days = []

# Commit until February 2024
end_day = 31  # We are working with January and February 2024, so day 31 is the limit

# Randomly select commit days (mimicking natural spacing)
while commit_count < total_commits and current_day <= (31 + 31):  # Until February 2024
    commit_days.append(current_day)

    # Skip 2-3 days (randomly), ensuring it doesn't exceed the end day
    current_day += randint(2, 3)
    
    if current_day <= (31 + 31):
        commit_count += 1

# Iterate through the selected commit days and simulate commits
for i in commit_days:
    # Commit on a random number of times for each day (between 1 and 3 commits)
    for j in range(randint(1, 3)):
        # Create a commit message with the selected day (e.g., "25 days ago")
        commit_date = str(i) + " days ago"
        
        # Write to file.txt (simulating some change on each commit)
        with open('file.txt', 'a') as f:
            f.write(commit_date + '\n')
        
        # Commit with the generated commit date
        os.system(f'git add .')
        os.system(f'git commit --date="{commit_date}" -m "Normal commit on {commit_date}"')

# Push to the remote repository
os.system('git push -u origin main')

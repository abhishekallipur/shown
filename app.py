import os
from random import randint, choice
from datetime import datetime, timedelta

def get_commit_count_for_day(date):
    """
    Returns the number of commits to make for a given day based on the activity pattern.
    The pattern follows the intensity shown in the contribution graph:
    0 = no commits (dark squares)
    1 = light activity (lightest green)
    2 = medium activity (medium green)
    3 = high activity (darkest green)
    """
    # Dictionary mapping months to their activity patterns
    # Each sub-list represents [Monday, Wednesday, Friday] activity levels
    monthly_patterns = {
        1: [[1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 1]],  # January
        2: [[1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 0, 0]],  # February
        3: [[0, 1, 1], [1, 0, 0], [0, 1, 1], [0, 0, 1]],  # March
        4: [[1, 0, 0], [1, 1, 0], [0, 0, 1], [1, 0, 0]],  # April
        5: [[0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 1, 0]],  # May
        6: [[1, 1, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0]],  # June
        7: [[2, 1, 0], [1, 1, 1], [1, 0, 1], [1, 1, 0]],  # July
        8: [[1, 1, 1], [0, 1, 0], [1, 1, 0], [1, 0, 1]],  # September
        9: [[0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 1]],  # October
        10: [[1, 1, 0], [0, 1, 1], [1, 0, 1], [0, 1, 0]], # November
        11: [[1, 0, 1], [1, 1, 0], [0, 1, 1], [1, 0, 0]], # December
        12: [[0, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 1]]  # Next December
    }
    
    month = date.month
    # Calculate which week of the month (0-3)
    week = (date.day - 1) // 7
    # Calculate day position (0 for Monday, 1 for Wednesday, 2 for Friday)
    day_position = {0: 0, 2: 1, 4: 2}[date.weekday()]
    
    if week < len(monthly_patterns[month]):
        return monthly_patterns[month][week][day_position]
    return 0

def create_commit(date, commit_number=1):
    """Creates a commit with the specified date"""
    commit_date_str = date.strftime('%Y-%m-%d %H:%M:%S')
    # Add some randomness to commit times during the day
    hour = randint(9, 17)  # Between 9 AM and 5 PM
    minute = randint(0, 59)
    second = randint(0, 59)
    commit_date = date.replace(hour=hour, minute=minute, second=second)
    commit_date_str = commit_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Write to file.txt
    with open('file.txt', 'a') as f:
        f.write(f"Commit {commit_number} on {commit_date_str}\n")
    
    # Create the commit
    os.system(f'git add .')
    os.system(f'git commit --date="{commit_date_str}" -m "Update {commit_number} on {commit_date_str}"')

# Start date (January 1st, 2024)
current_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)

# Iterate through each day of the year
while current_date <= end_date:
    # Only commit on Monday (0), Wednesday (2), and Friday (4)
    if current_date.weekday() in [0, 2, 4]:
        commit_count = get_commit_count_for_day(current_date)
        
        # Create the specified number of commits for this day
        for i in range(commit_count):
            create_commit(current_date, i + 1)
    
    # Move to next day
    current_date += timedelta(days=1)

# Push changes to remote repository
os.system('git push -u origin main')
statistics = {
    "total_tasks": 0,
    "completed_tasks": 0,
    "users": {}
}

def update_statistics(user_email: str, completed: bool):
    """Update statistics dynamically based on user activity."""
    # Update total tasks
    statistics["total_tasks"] += 1

    # Update completed tasks if applicable
    if completed:
        statistics["completed_tasks"] += 1

    # Update user-specific statistics
    if user_email not in statistics["users"]:
        statistics["users"][user_email] = {"tasks": 0}
    statistics["users"][user_email]["tasks"] += 1

def get_statistics():
    """Retrieve current statistics."""
    return statistics
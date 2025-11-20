# =====================================================
# Task Prioritization System
# License: MIT License
# =====================================================
# This script calculates and displays the priority of a list of tasks.
# Each task has a name, duration, and urgency level.
# The algorithm assigns a score to each task and sorts them accordingly.
# =====================================================

from typing import List, Dict, Any


def validate_tasks(tasks: List[Dict[str, Any]]) -> bool:
    """
    Validate that all tasks have correct structure and values.

    Args:
        tasks (List[Dict[str, Any]]): List of task dictionaries.

    Returns:
        bool: True if all tasks are valid, False otherwise.
    """
    for task in tasks:
        if not all(key in task for key in ["name", "duration", "urgency"]):
            print(f" Missing keys in task: {task}")
            return False
        if not isinstance(task["duration"], (int, float)) or task["duration"] <= 0:
            print(f" Invalid duration in task: {task['name']}")
            return False
        if not isinstance(task["urgency"], int) or not (1 <= task["urgency"] <= 5):
            print(f" Urgency must be between 1 and 5 in task: {task['name']}")
            return False
    return True


def calculate_priority(duration: float, urgency: int) -> float:
    """
    Calculate the priority score for a task.

    Args:
        duration (float): Estimated time in minutes.
        urgency (int): Urgency level from 1 (low) to 5 (high).

    Returns:
        float: Calculated priority score.
    """
    # The formula combines urgency and inverse of duration
    priority = urgency * 2 + (60 / duration)
    return round(priority, 2)


def assign_priorities(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Assign a priority score to each task.

    Args:
        tasks (List[Dict[str, Any]]): List of tasks.

    Returns:
        List[Dict[str, Any]]: Same list but with added 'priority' key.
    """
    for task in tasks:
        task["priority"] = calculate_priority(task["duration"], task["urgency"])
    return tasks


def sort_tasks_by_priority(tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Sort tasks in descending order of priority.

    Args:
        tasks (List[Dict[str, Any]]): List of tasks with 'priority'.

    Returns:
        List[Dict[str, Any]]: Sorted list of tasks.
    """
    return sorted(tasks, key=lambda x: x["priority"], reverse=True)


def display_tasks(tasks: List[Dict[str, Any]]) -> None:
    """
    Display tasks neatly formatted.

    Args:
        tasks (List[Dict[str, Any]]): List of tasks to display.
    """
    print("\n📋 Recommended Task Order:")
    print("-" * 45)
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']:<20} | Urgency: {task['urgency']} | "
              f"Duration: {task['duration']} min | Priority: {task['priority']}")
    print("-" * 45)


def main() -> None:
    """
    Main function to run the task prioritization algorithm.
    """
    # Example list of tasks (you could later load these dynamically)
    tasks = [
        {"name": "Finish report", "duration": 120, "urgency": 5},
        {"name": "Email client", "duration": 15, "urgency": 4},
        {"name": "Clean desk", "duration": 20, "urgency": 2},
        {"name": "Study Python", "duration": 60, "urgency": 3},
        {"name": "Team meeting", "duration": 45, "urgency": 5}
    ]

    print(" Starting Task Prioritization System...")

    # Step 1: Validate task data
    if not validate_tasks(tasks):
        print(" Task list invalid. Exiting program.")
        return

    # Step 2: Assign priorities
    tasks_with_priorities = assign_priorities(tasks)

    # Step 3: Sort tasks
    sorted_tasks = sort_tasks_by_priority(tasks_with_priorities)

    # Step 4: Display final list
    display_tasks(sorted_tasks)


# Entry point
if __name__ == "__main__":
    main()




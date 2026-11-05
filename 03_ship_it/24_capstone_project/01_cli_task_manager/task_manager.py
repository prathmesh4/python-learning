import json
import os
import shlex
from pathlib import Path

DATA_FILE = Path("03_ship_it") / "24_capstone_project" / "01_cli_task_manager" / "tasks.json"
PRIORITIES = ["low", "medium", "high"]
#File Handling
def load_tasks():
    """Load tasks from the JSON file."""
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
        if not isinstance(data, list):
            print("Warning: Invalid task data. Starting with an empty list.")
            return []
        tasks = []
        for task in data:
            if (
                isinstance(task, dict)
                and isinstance(task.get("id"), int)
                and isinstance(task.get("title"), str)
                and isinstance(task.get("priority"), str)
                and task.get("priority") in PRIORITIES
                and isinstance(task.get("done"), bool)
            ):
                tasks.append(task)
        return tasks
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read tasks.json. Starting empty.")
        return []
def save_tasks(tasks):
    """Save tasks safely to JSON."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temp_file = DATA_FILE.with_suffix(".tmp")
    try:
        with temp_file.open("w") as file:
            json.dump(tasks, file, indent=4)
        temp_file.replace(DATA_FILE)
    except OSError as error:
        print(f"Error saving tasks: {error}")
        if temp_file.exists():
            try:
                temp_file.unlink()
            except OSError:
                pass
#Task Operations
def add_task(tasks, title, priority):
    if not title.strip():
        print("Error: Task title cannot be empty.")
        return
    if priority not in PRIORITIES:
        print("Error: Priority must be low, medium, or high.")
        return
    next_id = max((task["id"] for task in tasks), default=0) + 1
    task = {
        "id": next_id,
        "title": title.strip(),
        "priority": priority,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{next_id} ({priority})")
def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return
    print("\n========== YOUR TASKS ==========")
    for task in tasks:
        status = "✓" if task["done"] else " "
        print(
            f"[{status}] #{task['id']}  "
            f"{task['title']:<25} ({task['priority']})"
        )
    print("================================")
def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print(f"Task #{task_id} is already complete.")
                return
            task["done"] = True
            save_tasks(tasks)
            print(f"✓ #{task_id} marked complete")
            return
    print(f"Error: Task #{task_id} not found.")
def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task #{task_id} deleted.")
            return
#Command Processing
def process_command(command, tasks):
    try:
        parts = shlex.split(command)
    except ValueError:
        print("Invalid command syntax. Check your quotation marks.")
        return True
    if not parts:
        return True
    action = parts[0].lower()
    if action in ("1", "add"):
        if len(parts) >= 2:
            title = " ".join(parts[1:-1])
            priority = parts[-1].lower()
            if priority not in PRIORITIES:
                print("Usage: add \"Task title\" low|medium|high")
            elif not title:
                print("Please provide a task title.")
            else:
                add_task(tasks, title, priority)
        else:
            print('Usage: add "Task title" high')
    elif action in ("2", "list"):
        list_tasks(tasks)
    elif action in ("3", "done"):
        if len(parts) == 2:
            try:
                task_id = int(parts[1])
                complete_task(tasks, task_id)
            except ValueError:
                print("Error: Task ID must be a number.")
        else:
            print("Usage: done <task_id>")
    elif action in ("4", "delete"):
        if len(parts) == 2:
            try:
                task_id = int(parts[1])
                delete_task(tasks, task_id)
            except ValueError:
                print("Error: Task ID must be a number.")
        else:
            print("Usage: delete <task_id>")
    elif action in ("5", "quit", "exit"):
        print("Goodbye! Your tasks have been saved.")
        return False
    elif action == "help":
        print_help()
    else:
        print("Unknown command. Type 'help' to see commands.")
    return True
#menu
def print_menu():
    print("\n========== TASK MANAGER ==========")
    print("1) Add")
    print("2) List")
    print("3) Done")
    print("4) Delete")
    print("5) Quit")
    print("==================================")
def print_help():
    print("""
Available commands:

  add "Finish capstone" high
  list
  done 1
  delete 1
  help
  quit

Priorities: low, medium, high
""")
def main():
    tasks = load_tasks()
    print("\nWelcome to CLI Task Manager!")
    print(f"Loaded {len(tasks)} task(s).")
    running = True
    while running:
        print_menu()
        try:
            command = input("> ").strip()
            running = process_command(command, tasks)
        except KeyboardInterrupt:
            print("\nUse 'quit' to exit safely.")
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as error:
            print(f"Something went wrong: {error}")

if __name__ == "__main__":
    main()
    
"""CLI Task Manager
Turning many small skills into one working tool
Build a command-line task manager a real person could use every day. This ties together input handling, data structures, functions, files, and error handling.

Requirements:
• Add, list, complete, and delete tasks
• Each task has a title, a priority, and a done/not-done state
• Persist tasks to a JSON file so they survive restarts
• A clean menu loop that never crashes on bad input

Example:

1) Add  2) List  3) Done  4) Delete  5) Quit
> add "Finish capstone" high
Added task #1 (high)
> list
[ ] #1  Finish capstone        (high)
> done 1
✓ #1 marked complete

Ship it with a short README explaining how to run it."""    
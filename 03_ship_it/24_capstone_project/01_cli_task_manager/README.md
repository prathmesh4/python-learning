
# CLI Task Manager

A simple command-line task manager built with Python.

## Features

- Add tasks with titles and priorities.
- List all tasks.
- Mark tasks as completed.
- Delete tasks.
- Save tasks automatically in a JSON file.
- Load saved tasks when restarting.
- Handle invalid commands and input errors.

## Requirements

- Python 3.8 or newer.
- No external libraries required.

## How to Run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

   python task_manager.py

## Available Commands

| Command | Description |
|---------|-------------|
| add "Task" high | Add a high-priority task |
| list | Display all tasks |
| done 1 | Complete task #1 |
| delete 1 | Delete task #1 |
| help | Show available commands |
| quit | Exit the application |

## Priority Levels

- low
- medium
- high

## Data Storage

Tasks are automatically stored in `tasks.json`.

Your tasks remain saved even after closing the application.

## Example

> add "Finish capstone" high

Added task #1 (high)

> list

[ ] #1 Finish capstone (high)

> done 1

✓ #1 marked complete

> quit

Goodbye! Your tasks have been saved.

## License

Free to use and modify for learning purposes.

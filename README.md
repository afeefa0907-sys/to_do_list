# to_do_list
A simple command-line to-do list checker in Python. Add tasks, mark them as done, and save the result to a text file.
# To-Do List Checker

A simple command-line to-do list program written in Python. You enter your tasks, mark them as completed, and the final status of every task is saved to a text file.

## Features

- Add any number of tasks at the start
- Mark tasks as done by typing their name
- Task names are cleaned up automatically (uppercased, extra spaces removed)
- Shows the list again if you type a task that does not exist
- Saves the final list to `to_do_file.txt`

## Requirements

- Python 3.6 or higher (no external libraries needed)



## How It Works

1. Enter how many tasks you want to add.
2. Type each task when prompted.
3. Type the name of a task to mark it as completed.
4. Type `done` when you want to stop.
5. The final list is saved to `to_do_file.txt`.

## Example

```
Hello and welcome to my to do list checker
How many tasks you want to add? 2
Enter your task no. 1: study python
Enter your task no. 2: go for a walk
{'STUDY PYTHON': False, 'GO FOR A WALK': False}
Type 'done' to stop;
Enter to task you want to check :> study python
Type 'done' to stop;
Enter to task you want to check :> done
{'STUDY PYTHON': True, 'GO FOR A WALK': False}
```

Contents of `to_do_file.txt`:

```
STUDY PYTHON: True
GO FOR A WALK: False
```

## Concepts Used

- Dictionaries
- Loops (`for`, `while`)
- User input and string methods
- File handling with `open()` and `with`



# Task Manager App

A simple and efficient task management application built with **Streamlit** that allows you to create, manage, and track your daily tasks.

## Features

✨ **Easy Task Management**

- ➕ Add new tasks quickly with an intuitive input field
- ✅ Mark tasks as complete by checking them off
- 📝 View all your tasks in a clean, organized interface
- 💾 Persistent storage of tasks in a local text file

## Requirements

- Python >= 3.14
- Streamlit >= 1.52.1

## Installation

1. **Clone or navigate to the project directory:**

   ```bash
   cd todo-app
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Or if using pyproject.toml:

   ```bash
   pip install -e .
   ```

## Usage

Run the Streamlit app with the following command:

```bash
streamlit run web.py
```

The app will open in your default web browser at `http://localhost:8501`.

### How to Use

1. **View Your Tasks**: All your tasks will be displayed on the main screen
2. **Add a New Task**: Enter your task in the "Add a new todo..." input field and press Enter
3. **Complete a Task**: Check the checkbox next to a task to mark it as complete and remove it from your list
4. **Tasks are Saved**: Your tasks are automatically saved to `todos.txt`

## Project Structure

```text
todo-app/
├── web.py                 # Main Streamlit application
├── modules/
│   └── reusableFuncs.py  # Utility functions for reading/writing tasks
├── todos.txt             # File where tasks are stored (created automatically)
├── pyproject.toml        # Project configuration and dependencies
└── README.md             # This file
```

## How It Works

### Core Functions

**`modules/reusableFuncs.py`**

- `get_todos(filepath)`: Reads all tasks from the `todos.txt` file and returns them as a list
- `write_todos(todos_arg, filepath)`: Saves the task list to the `todos.txt` file

### Main App Flow

The `web.py` file uses Streamlit to:

1. Load existing tasks from the file
2. Display them with checkboxes for completion
3. Add new tasks via text input
4. Remove completed tasks
5. Persist all changes to storage

## Future Enhancements

- 📅 Add due dates to tasks
- 🏷️ Implement task categories/tags
- 🎯 Add priority levels
- 🔔 Add task reminders
- 🌙 Dark mode support
- 📊 Task completion statistics

## License

This project is open source and available for personal use.

## Support

For any issues or questions, please check the code or reach out with your feedback!

---

**Happy task managing!** 🚀

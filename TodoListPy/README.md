# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows you to manage your tasks by adding, viewing, marking as complete, and deleting tasks. Additionally, it supports task prioritization and saving tasks to a JSON file.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Features](#features)
- [Usage](#usage)
- [Sample tasks.json](#sample-tasksjson)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before running the application, make sure you have Python 3 installed on your system.

## Features

- Add tasks with titles, due dates, and priorities.
- View tasks, sorted by completion status, priority, and due date.
- Mark tasks as complete.
- Delete tasks.
- Save and load tasks to/from a JSON file.
- Simple and easy-to-use command-line interface.

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Run the To-Do List application:

   ```bash
   python todo_app.py
Follow the on-screen prompts to interact with the application.
Sample tasks.json
You can create a tasks.json file in the project directory to store your tasks. Here's an example of the JSON format for tasks:

json
Copy code
[
    {
        "title": "Complete Python project",
        "due_date": "2023-09-10",
        "priority": 3,
        "completed": false
    },
    {
        "title": "Buy groceries",
        "due_date": "2023-09-06",
        "priority": 2,
        "completed": false
    },
    {
        "title": "Read a book",
        "due_date": "2023-09-15",
        "priority": 1,
        "completed": true
    }
]
You can add, modify, or delete tasks in this JSON file.

Contributing
Contributions are welcome! If you'd like to improve this To-Do List application or add new features, please open an issue or create a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

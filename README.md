# Task Management API

A RESTful API for managing users, projects, and tasks. Built with Flask, SQLAlchemy, and Marshmallow. Designed for learning and demonstration, with intentional bugs and missing features for practice.

## Features
- User registration and login (JWT authentication)
- CRUD for tasks and projects
- Assign tasks to users
- Filter tasks by status, project, or user

## Known Bugs
- Task status update does not check if user is assigned
- Project deletion does not cascade to tasks

## Missing Features
- Password reset
- Pagination on task list
- Email notifications

## Tech Stack
- Python 3.x
- Flask
- SQLAlchemy
- Marshmallow
- SQLite
- pytest
- python-dotenv
- Werkzeug

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env` and update as needed.

5. **Run the application:**
   ```bash
   flask run
   ```

6. **Run tests:**
   ```bash
   pytest
   ```

## Contribution Guide
- Fork the repository and create a new branch for your feature or bugfix.
- Write clear, concise commit messages.
- Add or update tests for your changes.
- Ensure code follows PEP8 and is well-documented.
- Submit a pull request with a description of your changes.

---

This project is for educational purposes and includes intentional bugs and missing features for practice. 
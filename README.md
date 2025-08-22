# Flask Task App

A simple and elegant task management web application built with Python and the Flask framework. This project demonstrates foundational web development concepts, including user authentication, database management, and form handling.

## Features

* **Task Management:** Create, delete, and mark tasks as complete.
* **User Authentication:** Secure user registration, login, and logout. Each user has a personalized, private to-do list.
* **Database Integration:** Uses **SQLAlchemy** to store and manage tasks and user data in an SQLite database.
* **Form Handling:** Secure and robust form validation with **Flask-WTF**.
* **Styling:** A clean and responsive user interface styled with **Bootstrap**.

## Technologies Used

* Python 3
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-WTF
* Bootstrap 5

## Getting Started

Follow these steps to set up and run the application on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/shahaj90/flask-task-app.git
```
```bash
cd flask-task-app
```

### 2. Create a virtual environment and activate it

```bash
python3 -m venv .venv
```

On Windows:
```bash
.\venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Initialize the database

```bash
flask db upgrade
```

### 6. Run the application

```bash
python3 run.py
```

The application will be accessible at `http://127.0.0.1:5000/` in your web browser.

## Project Structure

```
flask-task-app/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── register.html
│       └── tasks.html
├── migrations/
├── .venv/
├── config.py
├── requirements.txt
├── run.py
└── README.md

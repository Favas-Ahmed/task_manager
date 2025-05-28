Task Manager

A simple and intuitive task management web application built with Django. This project allows users to create, update, and delete tasks, helping them manage their daily activities efficiently.

🚀 Features

Task Management: Create, read, update, and delete tasks.

User Authentication: Secure user registration and login system.

Responsive Design: Accessible on various devices, including desktops, tablets, and mobile phones.

SQLite Database: Lightweight and easy-to-use database for development purposes.


🛠 Technologies Used

Python

Django

HTML

CSS

SQLite


📂 Project Structure

task_manager/
├── manage.py
├── db.sqlite3
├── regapp/
├── static/
├── templates/
├── todoapp/
└── todoproject/

manage.py: Django's command-line utility for administrative tasks.

db.sqlite3: SQLite database file.

regapp/: Handles user registration and authentication.

todoapp/: Core application managing tasks.

todoproject/: Main project configuration.

templates/: HTML templates for rendering views.

static/: Static files like CSS and JavaScript.


🔧 Installation

1. Clone the Repository

git clone https://github.com/Favas-Ahmed/task_manager.git
cd task_manager


2. Create a Virtual Environment

python -m venv env


3. Activate the Virtual Environment

On Windows:

env\Scripts\activate

On macOS and Linux:

source env/bin/activate



4. Install Dependencies

pip install django

Note: If a requirements.txt file is available, use pip install -r requirements.txt instead.


5. Apply Migrations

python manage.py migrate


6. Run the Development Server

python manage.py runserver

Access the application at http://127.0.0.1:8000/.



🧪 Usage

Navigate to the homepage.

Register a new account or log in with existing credentials.

Create new tasks, update existing ones, or delete tasks as needed.


🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

📄 License

This project is open-source and available under the MIT License.

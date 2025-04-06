 Restaurant Finder App

A simple web app that helps users find restaurants based on location, cuisine, and price range.

 Features

- List of restaurants with details
- Filter by cuisine and max price
- API built with Django REST Framework
- JWT authentication for secure access
- Simple HTML frontend for display

Tech Stack

- Django & Django REST Framework
- SQLite (default) or any preferred DB
- HTML/CSS (basic template)
- JWT for auth (via SimpleJWT)

 Setup

1. Clone the repo  
2. Run `pip install -r requirements.txt`  
3. Apply migrations: `python manage.py migrate`  
4. Create a superuser: `python manage.py createsuperuser`  
5. Start server: `python manage.py runserver`  
6. Visit: `http://127.0.0.1:8000/`




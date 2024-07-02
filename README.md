# Blog Project

This is a Django-based blog application that allows users to create, edit, and view blog posts. The application uses PostgreSQL as its database backend.

## Features

- Create, edit, and delete blog posts
- View all blog posts on the `/blog/` endpoint
- Admin interface for managing blog posts
- RESTful API for fetching blog posts

## Requirements

- Python 3.8+
- Django 5.0.6
- PostgreSQL

## Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Bakkenti/blog_project
    cd blog_project
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate   # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Create a `.env` file in the root directory of the project with the following content:**

    ```plaintext
    DEBUG=True/False
    SECRET_KEY=example
    DATABASE_URL=postgres://postgres:password@host:port/db_name
    ```

5. **Run database migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a superuser for accessing the admin interface:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

9. **Access the application:**

    - Blog page: `http://127.0.0.1:8000/blog/`
    - Admin interface: `http://127.0.0.1:8000/admin/`

## Deployment

When deploying to production, make sure to set `DEBUG=False` in your `.env` file and configure the allowed hosts appropriately.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

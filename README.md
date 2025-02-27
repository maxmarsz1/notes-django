# NoteTakingApp

Minimalistic web app developed in ReactJS and Django. My first try on working with Rest Framework, and at the same time learning React basics.

# Setup

## Prerequisites

* **Python:** (e.g., Python 3.9+)
* **pip:** (Python package installer)
* **Docker** (if using Docker-based setup)
* **Docker Compose** (if using Docker Compose)

## Instalation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/maxmarsz1/notes-django.git
    cd notes-django
    ```

2. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

    * This will build the Docker images and start the containers, including the database and pgAdmin.
    * To access pgAdmin, go to `http://localhost:5050`

3.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

4.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5.  **Configure the database:**

    * Create a PostgreSQL database (or other database as configured in `settings.py`).
    * Update the `DATABASES` settings in `settings.py` with your database credentials.

6.  **Run migrations:**

    ```bash
    python manage.py migrate
    ```

7.  **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

8.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    * The application will be accessible at `http://localhost:8000`.


## What I've learned so far

Django Rest Framework:

- APIViews
- ModelViewsets
- Permissions
- SimpleJWT concept (how tokens are structured, what is refresh token rotating, what are sliding tokens, token blacklisting)

## Things that still needs to be done:

- Optimisations

Optional:

- Page transitions
- Animations


Done:

- ~~Feedback (Disabling button on press, etc.)~~
- ~~Information when data is loading~~
- ~~Mobile support (responsive design)~~

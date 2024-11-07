# My Django App

This is a Django web application designed to demonstrate a simple setup, including running within a Docker container. The application includes example views, models, and templates, and is configured to use Docker for easy deployment.

## Features

- Built with Django
- Dockerized for easy container-based deployment
- Optional setup with PostgreSQL using Docker Compose

## Prerequisites

- Docker and Docker Compose installed on your system

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/my-django-app.git
cd my-django-app
```

### 2. Install Dependencies
Install on dependencies using the requirements.txt file
```
pip install -r requirements.txt
```

### 3. Running the Application in Docker

**Using Docker only (SQLite as default)**
    1. Build the Docker image:
    ```
    docker build -t hello .

    ```
    2. Run the Docker container
    ```
    docker run -p 8000:8000 hello
    ```
The application will be availabe at http://127.0.0.0.1:8000

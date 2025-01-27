
# Flask To-Do Application

## Introduction
This is a Flask-based project that allows you to create users, create tasks, and fetch tasks associated with a specific user. The application uses SQLAlchemy for ORM-based database management and a PostgreSQL database for storing data.

## Prerequisites
Before setting up the project, ensure you have the following installed on your system:

- Python 3.12 or higher
- PostgreSQL (or another database set up as per SQLAlchemy configuration)
- Poetry for dependency management
- Docker for containerization

## Installation Steps

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Build and Run the Docker Containers
Use the following commands to build and start the containers:

```bash
docker-compose build
docker-compose up
```

### 3. Check for Available Ports (If Necessary)
If you encounter issues with the default ports, you can check for availability and free up the ports as follows:

```bash
sudo lsof -i:5432
sudo kill -9 <process_id>
```

## Testing
Once the application is running, you can test it by accessing the following URL in your browser:

[http://127.0.0.1:8000](http://127.0.0.1:8000)

## Additional Notes
This Flask app allows you to create users, create tasks, and retrieve tasks for a specific user. The project utilizes SQLAlchemy for database interaction and PostgreSQL for storing the data effectively.






# FLask

This is a Flask-based project that allows you to create users and tasks and fetch tasks associated with a specific user. The application uses SQLAlchemy for ORM-based database management, with a PostgreSQL database.

## Prerequisites
Python 3.12 or higher
PostgreSQL (or another database setup as per SQLAlchemy configuration)
poetry for dependency management 
Docker Configration
Project Setup
## 1. Clone the Repository
First, clone this repository to your local machine:
bash
Copy
git clone <repository_url>

## Setup project

docker-compose build
docker-compose up

## check all port available if not
sudo lsof -i:5432
 sudo kill -9 950


## Test the app
Test the app on this url
http://127.0.0.1:8000







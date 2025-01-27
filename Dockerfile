# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

FROM python:3.12-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock  ./
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main --no-root


COPY app ./app

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]


# Run the application
# CMD ["flask", "run", "--host=0.0.0.0"]

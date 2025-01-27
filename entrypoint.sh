#!/bin/bash

# Check if the migration folder exists
if [ ! -d "migrations" ]; then
    echo "No migrations folder found. Creating migrations..."
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
else
    echo "Migrations folder exists. Checking for new migrations..."
    flask db migrate -m "Auto migration"
    flask db upgrade
fi


# Run the Flask app
exec flask run --host=0.0.0.0
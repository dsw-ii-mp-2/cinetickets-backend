#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Apply any outstanding database migrations
ls
python cinetickets-backend/cinetickets/manage.py makemigrations
python cinetickets-backend/cinetickets/manage.py migrate
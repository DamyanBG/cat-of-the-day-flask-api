# cat-of-the-day-flask-api

## Cat of the day app implemented with Flask RestAPI

This project is for learning purpose. The idea behind the project is to have simple cat social media with voting for cats and the cat which receives the most likes for the day will be the cat of the day!

## Run the application

1. Setup .env file with variables:
    - DB_USER
    - DB_PASSWORD
    - DB_HOST
    - DB_NAME
    - JWT_KEY
    - NEXTCLOUD_USER
    - NEXTCLOUD_PASSWORD
2. Export environment variable in Powershell (for Windows users, for other OS check the official Flask documentation) `$env:FLASK_APP = "main.py"`
3. On local use `flask run --reload --debug`
4. For production use Gunicorn.
This is the server part of the Project Hermod.

For the file .flaskenv to work is necessary to install:

pip install python-dotenv

** DB commands

Initialize db
flask db init

Generate migrations
flask db migrate -m "my first migration"

Upgrade database with migrations
flask db upgrade

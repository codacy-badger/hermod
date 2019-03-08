This is the server part of the Project Hermod. Is made in flask and the
project structure was mostly take from the [Project Real World](https://github.com/gothinkster/flask-realworld-example-app)

For the file .flaskenv to work is necessary to install:

```bash
pip install python-dotenv
```

For better experience is advisable that the server is run from a virtual environment.

#### DB commands

Commands to execute if you want to:

Initialize db

```bash
flask db init
```

Generate migrations

```bash
flask db migrate -m "my first migration"
```

Upgrade database with migrations

```bash
flask db upgrade
```

#### Test

If you want to execute the tests just run the command:

```bash
flask test
```

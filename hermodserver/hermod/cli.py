# -*- coding: utf-8 -*-
import click
import os

HERE = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.join(HERE, os.pardir)
TEST_PATH = os.path.join(PROJECT_ROOT, 'tests')

def register(app):

    @app.cli.command()
    def clean():
        """Remove *.pyc and *.pyo files recursively starting at current directory.
        Borrowed from Flask-Script, converted to use Click.
        """
        for dirpath, _, filenames in os.walk('.'):
            for filename in filenames:
                if filename.endswith('.pyc') or filename.endswith('.pyo'):
                    full_pathname = os.path.join(dirpath, filename)
                    click.echo('Removing {}'.format(full_pathname))
                    os.remove(full_pathname)

    @app.cli.command()
    def test():
        """Run the tests."""
        import pytest
        rv = pytest.main([TEST_PATH, '--verbose','--junitxml=pytest-report.xml','--cov=./','hermodserver.py','--cov-report','xml:coverage.xml'])
        exit(rv)

# -*- coding: utf-8 -*-
"""Model unit tests."""

import pytest

from hermod.user.models import User
from hermod.quote.models import Quote

from .factories import UserFactory

@pytest.mark.usefixtures('db')
class TestUser:
    """User tests."""

    def test_get_by_id(self):
        """Get user by ID."""
        user = User('foo', 'foo@bar.com')
        user.save()

        retrieved = User.get_by_id(user.id)
        assert retrieved == user

    def test_get_by_username(self):
        """Get user by ID."""
        user = User('foo', 'foo@bar.com')
        user.save()

        retrieved = User.get_user_by_username(user.username)
        assert retrieved == user

    def test_password_is_nullable(self):
        """Test null password."""
        user = User(username='foo', email='foo@bar.com')
        user.save()
        assert user.password is None

    def test_factory(self, db):
        """Test user factory."""
        user = UserFactory(password='myprecious')
        db.session.commit()
        assert bool(user.username)
        assert bool(user.email)
        assert user.check_password('myprecious')

    def test_check_password(self):
        """Check password."""
        user = User.create(username='foo', email='foo@bar.com',
                           password='foobarbaz123')
        assert user.check_password('foobarbaz123')
        assert not user.check_password('barfoobaz')

@pytest.mark.usefixtures('db')
class TestQuote:

    def test_make_quote(self):
        quote = Quote(author="Dr test",body="Is always good to tdd")
        quote.save()
        assert quote.author == "Dr test"

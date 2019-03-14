# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, flash

from flask_login import current_user, login_user, logout_user
from hermod.user.models import User
from hermod.home.forms import LoginForm

blueprint = Blueprint('home', __name__)


@blueprint.route('/')
@blueprint.route('/index')
def index():
    return render_template("index.html", title='Home Page')


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('home.login'))
        login_user(user)
        return redirect(url_for('home.index'))
    return render_template('auth/login.html', title='Sign In', form=form)


@blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home.index'))

# app/routes.py

from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm, RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required
from app.models import User

@app.route('/')
@app.route('/profile')
@login_required
def profile():
    """Profile page"""
    return render_template('profile.html', title='Profile')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('Welcome')
        return redirect(url_for('profile'))
    return render_template('login.html', title='Login', form=form)
    
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from app import db
from app.forms import RegistrationForm
from app.models import User

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Registered successfully. Please log in to continue.')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred while registering. Please try again.')
            app.logger.error(f"Error during registration: {e}")
    
    return render_template('register.html', title='Register', form=form)

     
@app.route('/logout')
@login_required
def logout():
    """Used to log out a user"""
    logout_user()
    return redirect(url_for('login'))
    
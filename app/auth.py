from app import app
from . import db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from .models import User, Bet
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/sign-up", methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists.', category = 'error')
        elif len(email) < 4:
            flash('Email length must be greater than 3 characters.', category = 'error')
        elif len(first_name) < 2:
            flash('First name length must be greater than 1 character.', category = 'error')
        elif len(last_name) < 2:
            flash('Last name length must be greater than 1 character.', category = 'error')           
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:
            new_user = User(email=email, first_name= first_name, last_name=last_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember = True)
            #flash('Account created!', category='success')
            return redirect(url_for('index'))

    return render_template("sign_up.html", user=current_user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # first returns the first result
        user = User.query.filter_by(email=email).first()
        # if a user is found, check if password they typed in exists in the database
        if user:
            if check_password_hash(user.password, password):
                # flash('Logged in successfully!', category = 'success')
                # remembers that user is logged in until they clear their cache
                login_user(user, remember = True)
                return redirect(url_for('index'))
            else:
                flash('Incorrect password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')
        
    return render_template("login.html", user = current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
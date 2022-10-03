from flask import Blueprint, render_template, request, flash
from jinja2 import pass_eval_context

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater then 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('Name must be greater than 1.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t  match', category='error')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters.', category='error')
        else:
            flash('Account created.', category='success')
            # add user to database
            pass

    return render_template('sign_up.html')
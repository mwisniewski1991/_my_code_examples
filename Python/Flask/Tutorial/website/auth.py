from symbol import pass_stmt
from flask import Blueprint, render_template, request
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
            pass
        elif len(first_name) < 2:
            pass 
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            # add user to database
            pass

    return render_template('sign_up.html')
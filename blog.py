#!/usr/bin/env python3

from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

# >>> import secrets
# >>> secrets.token_hex(16)
app.config['SECRET_KEY'] = 'fd807ecee9774c7027daed87270b24ed'

posts = [
        {
            'author': 'Author Name',
            'title': 'Post 1',
            'content': 'some content',
            'date_posted': '14 June 2019'
        },
        {
            'author': 'Rob Name',
            'title': 'Post 2',
            'content': 'some content 2',
            'date_posted': '12 June 2019'
        }
        ]

@app.route('/')
@app.route('/home')
def  home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def  about():
    return render_template('about.html')

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)



from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from ..models import User
from . import main
from .forms import LoginForm, InputForm, SuggestionForm


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.verify_password(form.password.data):
            return redirect(url_for('main.login', **request.args))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('main.index'))
    return render_template('login.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/scan', methods=['GET', 'POST'])
@login_required
def scan():
    text_input, suggestions = InputForm(), SuggestionForm()
    choices = ("one", "two", "three")

    suggestions.suggestions.choices = [(i, x) for i, x in enumerate(choices)]

    if text_input.validate_on_submit():
        # TODO: Fix the logic here
        pass

    return render_template(
        'scan.html',
        text_input=text_input,
        suggestions=suggestions
    )

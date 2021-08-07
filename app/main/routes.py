from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
from app.models import User
from app.main.forms import LoginForm, InputForm, SuggestionForm
from app.settings import DEFAULT_VOCABULARY
from assistant.find import find
from . import main


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
    text_input, words = InputForm(), SuggestionForm()
    words.suggestions.choices = []

    if text_input.validate_on_submit():
        choices = find(
            text_input.translation.data,
            DEFAULT_VOCABULARY,
            only_nouns=False
        )
        print(choices)
        words.suggestions.choices = [(i, x) for i, x in enumerate(choices)]

    if len(words.suggestions.choices) > 0:
        filtered = [(w, w) for f, w in words.suggestions.choices if f < 1]
        words.suggestions.choices = filtered

    return render_template(
        'scan.html',
        text_input=text_input,
        words=words
    )

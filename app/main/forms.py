from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import SelectMultipleField
from wtforms.validators import Length, DataRequired

from wtforms.widgets import CheckboxInput, ListWidget


class LoginForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(1, 16)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class InputForm(FlaskForm):
    translation = StringField('', validators=[DataRequired()],
                              render_kw={'autofocus': True})
    submit = SubmitField('submit')


class SuggestionForm(FlaskForm):
    suggestions = SelectMultipleField(
        'OOV words',
        option_widget=CheckboxInput(),
        widget=ListWidget(prefix_label=False),
        choices=[],
    )
    filters = SubmitField('filter')

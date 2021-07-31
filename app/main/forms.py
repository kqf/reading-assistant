from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(1, 16)])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class InputForm(FlaskForm):
    translation = StringField('', validators=[DataRequired()],
                              render_kw={'autofocus': True})
    submit = SubmitField('submit')

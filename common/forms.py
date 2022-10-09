from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange, DataRequired, Length, EqualTo


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class RegistrationForm(Form):
    username = StringField('Username', [Length(min=4, max=25)])
    password = PasswordField(
        'New Password', [
            DataRequired(),
            Length(min=8),
            EqualTo('confirm', message='Passwords must match')
        ])
    confirm = PasswordField('Repeat Password')


class GameRSVPForm(FlaskForm):
    # TODO: make it so that users can't submit duplicate preferences

    position_choices = ["Outside Hitter", "Opposite Hitter", "Middle Blocker", "Libero", "Setter"]
    name = StringField("Name", validators=[InputRequired()])
    position_1 = SelectField("Preference 1", coerce=str, choices=position_choices, validators=[InputRequired()])
    position_2 = SelectField("Preference 2", coerce=str, choices=position_choices, validators=[InputRequired()])
    position_3 = SelectField("Preference 3", coerce=str, choices=position_choices, validators=[InputRequired()])
    years = IntegerField("Preference 3", validators=[NumberRange(min=0, max=122)])
    submit = SubmitField('Submit')

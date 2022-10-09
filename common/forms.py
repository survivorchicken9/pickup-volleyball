from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange, DataRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Login")


class GameRSVPForm(FlaskForm):
    # TODO: game_id = StringField("")  # need to get this from function not html later
    # TODO: make it so that users can't submit duplicate preferences

    position_choices = ["Outside Hitter", "Opposite Hitter", "Middle Blocker", "Libero", "Setter"]
    name = StringField("Name", validators=[InputRequired()])
    position_1 = SelectField("Preference 1", coerce=str, choices=position_choices, validators=[InputRequired()])
    position_2 = SelectField("Preference 2", coerce=str, choices=position_choices, validators=[InputRequired()])
    position_3 = SelectField("Preference 3", coerce=str, choices=position_choices, validators=[InputRequired()])
    years = IntegerField("Preference 3", validators=[NumberRange(min=0, max=122)])
    submit = SubmitField('Submit')

# < select
# id = "pos1"
#
#
# class ="form-select mx-auto w-auto mb-4 mt-4" name="pos1" >
#
# < option
# selected = "selected"
# disabled > Preference
# 1 < / option >
# < option > Outside
# Hitter < / option >
# < option > Opposite / Diagonal < / option >
# < option > Middle
# Hitter < / option >
# < option > Libero < / option >
# < option > Setter < / option >
# < / select >
# < select
# id = "pos2"
#
#
# class ="form-select mx-auto w-auto mb-4" name="pos2" >
#
# < option
# selected = "selected"
# disabled > Preference
# 2 < / option >
# < option > Outside
# Hitter < / option >
# < option > Opposite / Diagonal < / option >
# < option > Middle
# Hitter < / option >
# < option > Libero < / option >
# < option > Setter < / option >
# < / select >
# < select
# id = "pos3"
#
#
# class ="form-select mx-auto w-auto mb-4" name="pos3" >
#
# < option
# selected = "selected"
# disabled > Preference
# 3 < / option >
# < option > Outside
# Hitter < / option >
# < option > Opposite / Diagonal < / option >
# < option > Middle
# Hitter < / option >
# < option > Libero < / option >
# < option > Setter < / option >

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NewGameForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    submit = SubmitField('Start New Game')

class DifficultyForm(FlaskForm):
    difficulty = SelectField('Choose Difficulty', choices=[('easy', 'Easy'), ('normal', 'Normal'), ('hard', 'Hard'), ('hardcore', 'Hardcore')])
    submit = SubmitField('Continue')

class UniversityForm(FlaskForm):
    university_type = SelectField('Choose University Type', choices=[('public', 'Public'), ('private', 'Private')])
    submit = SubmitField('Continue')

class ProgramForm(FlaskForm):
    program = SelectField('Choose Program', choices=[('civil_engineering', 'Civil Engineering'), ('nursing', 'Nursing'), ('computer_science', 'Computer Science'), ('fine_arts', 'Fine Arts')])
    submit = SubmitField('Continue')

class DormForm(FlaskForm):
    dorm_type = SelectField('Choose Dorm Type', choices=[('solo_room', 'Solo Room'), ('bed_space', 'Bed Space')])
    submit = SubmitField('Continue')

class FirstScenarioForm(FlaskForm):
    choice = SelectField('Choose Decision', choices=[('a', ' '), ('b', ' ')])
    submit = SubmitField('Submit')

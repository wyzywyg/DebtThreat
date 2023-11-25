from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class ScenarioForm(FlaskForm):
    choice = SelectField('Choose Decision', choices=[], coerce=str)
    def __init__(self, choices=None, **kwargs):
        super(ScenarioForm, self).__init__(**kwargs)
        if choices:
            self.choice.choices = choices
            
class NewGameForm(FlaskForm):
    name = StringField('', validators=[DataRequired()])
    submit = SubmitField('Start New Game')

class DifficultyForm(FlaskForm):
    difficulty = SelectField('Choose Difficulty', choices=[('easy', 'Easy'), ('normal', 'Normal'), ('hard', 'Hard'), ('hardcore', 'Hardcore')])

class UniversityForm(FlaskForm):
    university_type = SelectField('Choose University Type', choices=[('public', 'Public'), ('private', 'Private')])

class ProgramForm(FlaskForm):
    program = SelectField('Choose Program', choices=[('civil_engineering', 'Civil Engineering'), ('nursing', 'Nursing'), ('computer_science', 'Computer Science'), ('fine_arts', 'Fine Arts')])

class DormForm(FlaskForm): 
    dorm_type = SelectField('Choose Dorm Type', choices=[('solo_room', 'Solo Room'), ('bed_space', 'Bed Space')])
    


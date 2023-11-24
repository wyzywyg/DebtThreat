from flask import Blueprint, render_template, redirect, url_for
from forms import NewGameForm, DifficultyForm, UniversityForm, ProgramForm, DormForm
from game_logic import GameLogic

index = Blueprint('index', __name__)

game_logic = GameLogic()

@index.route('/')
def home():
    return render_template('menu.html')

@index.route('/new_game', methods=['GET', 'POST'])
def new_game():
    form = NewGameForm()
    if form.validate_on_submit():
        player_name = form.name.data
        game_logic.initialize(player_name)
        return redirect(url_for('index.difficulty'))
    return render_template('new_game.html', form=form)

@index.route('/difficulty', methods=['GET', 'POST'])
def difficulty():
    form = DifficultyForm()
    if form.validate_on_submit():
        difficulty = form.difficulty.data
        game_logic.set_difficulty(difficulty)
        return redirect(url_for('index.university'))
    return render_template('difficulty.html', form=form)

@index.route('/university', methods=['GET', 'POST'])
def university():
    form = UniversityForm()
    if form.validate_on_submit():
        university_type = form.university_type.data
        game_logic.set_university(university_type)
        return redirect(url_for('index.program'))
    return render_template('university.html', form=form)

@index.route('/program', methods=['GET', 'POST'])
def program():
    form = ProgramForm()
    if form.validate_on_submit():
        program = form.program.data
        game_logic.set_program(program)
        return redirect(url_for('index.dorm'))
    program_costs = {
        'public': {
            'easy': {'civil_engineering': 60000, 'nursing': 80000, 'computer_science': 40000, 'fine_arts': 80000},
            'normal': {'civil_engineering': 80000, 'nursing': 100000, 'computer_science': 60000, 'fine_arts': 100000},
            'hard': {'civil_engineering': 120000, 'nursing': 140000, 'computer_science': 100000, 'fine_arts': 140000}
        },
        'private': {
            'easy': {'civil_engineering': 80000, 'nursing': 100000, 'computer_science': 60000, 'fine_arts': 100000},
            'normal': {'civil_engineering': 100000, 'nursing': 120000, 'computer_science': 80000, 'fine_arts': 120000},
            'hard': {'civil_engineering': 140000, 'nursing': 160000, 'computer_science': 120000, 'fine_arts': 160000},
            'hardcore': {'civil_engineering': 200000, 'nursing': 220000, 'computer_science': 180000, 'fine_arts': 220000}
        }
    }

    return render_template('program.html', form=form, university=university, difficulty=difficulty, program_costs=program_costs)


@index.route('/dorm', methods=['GET', 'POST'])
def dorm():
    form = DormForm()
    if form.validate_on_submit():
        dorm_type = form.dorm_type.data
        game_logic.set_dorm(dorm_type)
        return redirect(url_for('index.summary'))
    return render_template('dorm.html', form=form)

@index.route('/summary')
def summary():
    game_logic.update_points()
    return render_template('summary.html', game=game_logic)

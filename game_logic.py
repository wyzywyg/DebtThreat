class GameLogic:
    def __init__(self):
        self.player_name = ""
        self.difficulty = ""
        self.university_type = ""
        self.program = ""
        self.dorm_type = ""
        self.debt = 500000
        self.debt_money = 500000
        self.education = 0
        self.health = 0
        self.happiness = 0

    def initialize(self, player_name):
        self.player_name = player_name

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

        if difficulty == 'easy':
            self.education += 20
            self.health += 20
            self.happiness += 20
        elif difficulty == 'normal':
            self.education += 10
            self.health += 10
            self.happiness += 10
        elif difficulty == 'hard':
            self.education -= 10
            self.health -= 10
            self.happiness -= 10
        elif difficulty == 'hardcore':
            self.education -= 20
            self.health -= 20
            self.happiness -= 20
        # Adjust points in education, health, and happiness based on the chosen difficulty

    def set_university(self, university_type):
        if self.difficulty in ['easy', 'normal', 'hard']:
            # Allow the user to choose between public and private university options
            self.university_type = university_type
        elif self.difficulty == 'hardcore':
            # Limit the user to choose private university only
            self.university_type = 'private'

    def set_program(self, program):
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

        if program in program_costs[self.university_type][self.difficulty]:
            cost = program_costs[self.university_type][self.difficulty][program]
            self.debt_money -= cost
            self.program = program
            return cost
        else:
            return 0

    def set_dorm(self, dorm_type):
        dorm_costs = {
            'solo_room': 40000,
            'bed_space': 9600
        }

        if dorm_type in dorm_costs:
            cost = dorm_costs[dorm_type]
            self.debt_money -= cost
            self.dorm_type = dorm_type
        # Deduct the chosen dorm type's cost from debt_money and set as the new.

    def update_points(self):
        # Logic to update points based on the chosen difficulty, program, and dorm type
        pass

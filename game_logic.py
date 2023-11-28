
from account import Account
account = Account()

class GameLogic:
    def __init__(self):
        self.player_name = ""
        self.difficulty = ""
        self.university_type = ""
        self.program = ""
        self.dorm_type = ""
        self.answer = ""
        self.debt = 500000
        self.debt_money = 500000
        self.education = 0
        self.health = 0
        self.happiness = 0
        self.messages = []
        self.final_score = 0
        self.result = ""
        self.salary = 0
        self.money = 0

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

            # Add points based on the chosen university type
            if university_type == 'public':
                self.education += 10
                self.health += 10
                self.happiness += 10
            elif university_type == 'private':
                self.education += 20
                self.health += 20
                self.happiness += 20

        elif self.difficulty == 'hardcore':
            # Limit the user to choose private university only
            self.university_type = 'private'

            # Add points for hardcore difficulty and private university
            self.education += 30
            self.health += 30
            self.happiness += 30

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

    def set_scenario(self, answer, debt_money_delta, education_delta, health_delta, happiness_delta):
        self.answer = answer
        if answer == 'A':
            self.debt_money += debt_money_delta
            self.education += education_delta
            self.health += health_delta
            self.happiness += happiness_delta
        elif answer == 'B':
            self.debt_money +=debt_money_delta
            self.education += education_delta
            self.health += health_delta
            self.happiness += happiness_delta
            
        # Ensure that the points don't exceed 100
        self.education = min(self.education, 100)
        self.health = min(self.health, 100)
        self.happiness = min(self.happiness, 100)
        
        if self.health <= 10:
            self.debt_money -= 10000

    def set_result(self):
        self.final_score = self.education + self.health + self.happiness
        if self.education in range(0, 20):
            self.salary =  25000
        elif self.education in range(21, 40):
            self.salary =  35000
        elif self.education in range(41, 60):
            self.salary =  40000
        elif self.education in range(61, 80):
            self.salary =  50000
        elif 81 <= self.education <= 100:
            self.salary =  75000
        
        self.money = self.salary * 6 + self.debt_money
        
        if self.money > self.debt:
            self.result = "Win"
            account.save_user_data(self.player_name, self.final_score)
            
        if self.money < self.debt: 
            self.result = "Lose"
            account.save_user_data(self.player_name, self.final_score)
            
        
            

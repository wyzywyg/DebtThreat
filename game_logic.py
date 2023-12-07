#game_logic.py

from database import Database

from pointing_system import (
    EasyPointingSystem,
    NormalPointingSystem, 
    HardPointingSystem, 
    HardcorePointingSystem,
    PublicUniversityPointingSystem, 
    PrivateUniversityPointingSystem,
    ProgramCostSystem,
    CivilEngineeringProgramCost,
    NursingProgramCost,
    ComputerScienceProgramCost,
    FineArtsProgramCost
)

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
        self.messages = None
        self.final_score = 0
        self.result = ""
        self.salary = 0
        self.money = 0
        self.debt_money_cost = 0
        self.education_cost = 0
        self.health_cost = 0
        self.happiness_cost = 0

    def initialize(self, player_name):
        self.player_name = player_name
        

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

        if difficulty == 'easy':
            pointing_system = EasyPointingSystem()
            pointing_system.apply_points(self)
        elif difficulty == 'normal':
            pointing_system = NormalPointingSystem()
            pointing_system.apply_points(self)
        elif difficulty == 'hard':
            pointing_system = HardPointingSystem()
            pointing_system.apply_points(self)
        elif difficulty == 'hardcore':
            pointing_system = HardcorePointingSystem()
            pointing_system.apply_points(self)

    def set_university(self, university_type):
        self.university_type = university_type
        
        if university_type == 'public':
                pointing_system = PublicUniversityPointingSystem()
                pointing_system.apply_points(self)
        elif university_type == 'private':
                pointing_system = PrivateUniversityPointingSystem()
                pointing_system.apply_points(self)

    def set_program(self, program):
        self.program = program
        if self.university_type and self.difficulty:
            program_costs = {
                'civil_engineering': CivilEngineeringProgramCost(self.difficulty, self.university_type),
                'nursing': NursingProgramCost(self.difficulty, self.university_type),
                'computer_science': ComputerScienceProgramCost(self.difficulty, self.university_type),
                'fine_arts': FineArtsProgramCost(self.difficulty, self.university_type),
                # Add more programs as needed
            }

            pointing_system = program_costs.get(program, ProgramCostSystem(0))
            pointing_system.apply_cost(self)

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

    def set_scenario(self, answer, debt_money_cost, education_cost, health_cost, happiness_cost):
        self.answer = answer
        self.debt_money_cost = debt_money_cost
        self.education_cost = education_cost
        self.health_cost = health_cost
        self.happiness_cost = happiness_cost
        
        if answer == 'A':
            self.debt_money += debt_money_cost
            self.education += education_cost
            self.health += health_cost
            self.happiness += happiness_cost
        elif answer == 'B':
            self.debt_money += debt_money_cost
            self.education += education_cost
            self.health += health_cost
            self.happiness += happiness_cost
            
        # Ensure that the points don't exceed 100
        self.education = min(self.education, 100)
        self.health = min(self.health, 100)
        self.happiness = min(self.happiness, 100)
        
        if self.health <= 10:
            self.debt_money -= 10000

    def set_result(self):
        self.final_score = self.education + self.health + self.happiness
        
        if self.final_score in range(0, 80):
            self.salary =  25000
        elif self.final_score in range(81, 150):
            self.salary =  35000
        elif self.final_score in range(151, 199):
            self.salary =  40000
        elif self.final_score in range(200, 249):
            self.salary =  50000
        elif self.final_score in range (250, 400):
            self.salary =  75000
        
        self.money = self.salary * 6 + self.debt_money
          
        if self.money > self.debt:
            self.result = "Win"
            
        if self.money < self.debt: 
            self.result = "Lose"
        database = Database()
        database.save_user_data(self.player_name, self.final_score, self.difficulty, self.university_type, self.program, self.dorm_type,
                       self.debt, self.debt_money, self.education, self.health, self.happiness)
            
    def get_leaderboard(self):
        database = Database()
        leaderboard_data = database.fetch_leaderboard_data()
        return leaderboard_data
    
    def initialize_users_table(self):
        database = Database()
        database.initialize_users_table()
    
    

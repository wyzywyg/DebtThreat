# pointing_system.py

class ProgramCostSystem:
    def __init__(self, cost):
        self.cost = cost

    def apply_cost(self, game_logic):
        
        game_logic.debt_money -= self.cost

class SetProgramCost(ProgramCostSystem):
    def __init__(self, program, difficulty, university_type, cost):
        super().__init__(cost)
        self.program = program
        self.difficulty = difficulty
        self.university_type = university_type
        
        

# Difficulty Pointing Systems
class DifficultyPointingSystem:
    def __init__(self, education_points, health_points, happiness_points):
        self.education_points = education_points
        self.health_points = health_points
        self.happiness_points = happiness_points

    def apply_points(self, game_logic):
        game_logic.education += self.education_points
        game_logic.health += self.health_points
        game_logic.happiness += self.happiness_points

# University Pointing Systems
class UniversityPointingSystem:
    def __init__(self, education_points, health_points, happiness_points):
        self.education_points = education_points
        self.health_points = health_points
        self.happiness_points = happiness_points

    def apply_points(self, game_logic):
        game_logic.education += self.education_points
        game_logic.health += self.health_points
        game_logic.happiness += self.happiness_points

# Difficulty Pointing System Implementations
class EasyPointingSystem(DifficultyPointingSystem):
    def __init__(self):
        super().__init__(education_points=20, health_points=20, happiness_points=20)

class NormalPointingSystem(DifficultyPointingSystem):
    def __init__(self):
        super().__init__(education_points=15, health_points=15, happiness_points=15)

class HardPointingSystem(DifficultyPointingSystem):
    def __init__(self):
        super().__init__(education_points=10, health_points=10, happiness_points=10)

class HardcorePointingSystem(DifficultyPointingSystem):
    def __init__(self):
        super().__init__(education_points=5, health_points=5, happiness_points=5)

# University Pointing System Implementations
class PublicUniversityPointingSystem(UniversityPointingSystem):
    def __init__(self):
        super().__init__(education_points=15, health_points=5, happiness_points=10)

class PrivateUniversityPointingSystem(UniversityPointingSystem):
    def __init__(self):
        super().__init__(education_points=20, health_points=10, happiness_points=15)

# Program Cost Pointing System Implementations
class CivilEngineeringProgramCost(SetProgramCost):
    def __init__(self, difficulty, university_type):
        cost = 0  # Default cost if not found
        program_costs = {
            'public': {
                'easy': 60000,
                'normal': 80000,
                'hard': 120000,
                'hardcore': 140000,
            },
            'private': {
                'easy': 80000,
                'normal': 100000,
                'hard': 140000,
                'hardcore': 200000,
            }
        }
        if university_type in program_costs and difficulty in program_costs[university_type]:
            cost = program_costs[university_type][difficulty]
        super().__init__('civil_engineering', difficulty, university_type, cost)

class NursingProgramCost(SetProgramCost):
    def __init__(self, difficulty, university_type):
        cost = 0  # Default cost if not found
        program_costs = {
            'public': {
                'easy': 80000,
                'normal': 100000,
                'hard': 140000,
                'hardcore': 160000,
            },
            'private': {
                'easy': 100000,
                'normal': 120000,
                'hard': 160000,
                'hardcore': 220000,
            }
        }
        if university_type in program_costs and difficulty in program_costs[university_type]:
            cost = program_costs[university_type][difficulty]
        super().__init__('nursing', difficulty, university_type, cost)

class ComputerScienceProgramCost(SetProgramCost):
    def __init__(self, difficulty, university_type):
        cost = 0  # Default cost if not found
        program_costs = {
            'public': {
                'easy': 40000,
                'normal': 60000,
                'hard': 100000,
                'hardcore': 120000,
            },
            'private': {
                'easy': 60000,
                'normal': 80000,
                'hard': 120000,
                'hardcore': 180000,
            }
        }
        if university_type in program_costs and difficulty in program_costs[university_type]:
            cost = program_costs[university_type][difficulty]
        super().__init__('computer_science', difficulty, university_type, cost)

class FineArtsProgramCost(SetProgramCost):
    def __init__(self, difficulty, university_type):
        cost = 0  # Default cost if not found
        program_costs = {
            'public': {
                'easy': 80000,
                'normal': 100000,
                'hard': 140000,
                'hardcore': 160000,
            },
            'private': {
                'easy': 100000,
                'normal': 120000,
                'hard': 160000,
                'hardcore': 220000,
            }
        }
        if university_type in program_costs and difficulty in program_costs[university_type]:
            cost = program_costs[university_type][difficulty]
        super().__init__('fine_arts', difficulty, university_type, cost)

# scenarios.py

class Scenario:
    def __init__(self, options, outcomes):
        self.options = options
        self.outcomes = outcomes

class FinancialScenario(Scenario):
    pass

class EducationScenario(Scenario):
    pass

class HealthScenario(Scenario):
    pass

class HappinnessScenario(Scenario):
    pass

SCENARIO_DATA = {
    'AA': EducationScenario([('A', 'Buy New Textbooks'), ('B', 'Buy Used Textbooks')],
                                      {'A': (-10000, 15, 0, 15), 'B': (-5000, 3, 0, 0)}),

    'AB': FinancialScenario([('A', 'Accept'), ('B', 'Decline')],
                                      {'A': (5000, -5, -2, -2), 'B': (0, 5, 0, 6)}),

    'AC': EducationScenario([('A', 'Hire a Tutor'), ('B', 'Self-study')],
                                      {'A': (-8000, 10, 2, 10), 'B': (0, 3, 0, 0)}),

    'AD': FinancialScenario([('A', 'Apply for part-time job'), ('B', 'Join the workshop')],
                                      {'A': (7000, -10, -2, -3), 'B': (0, 10, 2, 9)}),

    'BA': EducationScenario([('A', 'Accept'), ('B', 'Decline')],
                          {'A': (0, 15, 5, 5), 'B': (5000, -15, -3, 2)}),

    'BB': HealthScenario([('A', 'Invest in gym membership'), ('B', 'Focus on Academics')],
                          {'A': (-15000, -5, 15, 5), 'B': (0, 5, -3, -5)}),

    'BC': HappinnessScenario([('A', 'Attend event'), ('B', 'Skip event')],
                          {'A': (-5000, 7, -2, 5), 'B': (0, 3, 10, -5)}),

    'BD': HealthScenario([('A', 'Take summer internship'), ('B', 'Take summer vacation')],
                          {'A': (7000, 7, 5, 5), 'B': (-5000, -7, 10, 5)}),

    'CA': FinancialScenario([('A', 'Pay with your loan'), ('B', 'Prioritize studies')],
                             {'A': (-50000, 0, 13, 10), 'B': (0, 5, -7, -10)}),

    'CB': FinancialScenario([('A', 'Accept'), ('B', 'Decline')],
                             {'A': (-85000, 15, 0, 5), 'B': (0, 5, 15, 5)}),

    'CC': FinancialScenario([('A', 'Time on relationship'), ('B', 'Prioritize studies')],
                             {'A': (-10000, -5, 15, 5), 'B': (0, 10, -5, -5)}),

    'CD': FinancialScenario([('A', 'Invest savings'), ('B', 'Research')],
                             {'A': (-30000, 15, -5, 5), 'B': (-5000, 5, -3, 3)}),

    'DA': EducationScenario([('A', 'Buy new laptop'), ('B', 'Stick with the current laptop')],
                                      {'A': (-50000, 15, 0, 15), 'B': (0, 2, 0, -2)}),

    'DB': EducationScenario([('A', 'Attend'), ('B', 'Decline')],
                                      {'A': (-25000, 10, 5, 10), 'B': (10000, -10, -5, -5)}),

    'DC': FinancialScenario([('A', 'Enroll in the course'), ('B', 'Self-study')],
                                      {'A': (-35000, 15, -5, 10), 'B': (0, 2, -2, -3)}),

    'DD': FinancialScenario([('A', 'Purchase new regalia'), ('B', 'Rent a set of regalia')],
                                      {'A': (-15000, 0, 0, 5), 'B': (-7500, 0, 0, 2)}),

    # Add more scenarios as needed...
}

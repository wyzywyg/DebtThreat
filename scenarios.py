# scenarios.py

SCENARIO_DATA = {
    'AA': {'options': [('A', 'Buy New Textbooks'), ('B', 'Buy Used Textbooks')],
           'outcomes': {'A': (-10000, 5, 0, 7), 'B': (-5000, 3, 0, 3)}},

    'AB': {'options': [('A', 'Accept'), ('B', 'Decline')],
           'outcomes': {'A': (5000, -5, -2, -2), 'B': (0, 2, -1, -1)}},

    'AC': {'options': [('A', 'Hire a Tutor'), ('B', 'Self-study')],
           'outcomes': {'A': (-8000, 5, 2, 2), 'B': (0, 2, -3, -2)}},

    'AD': {'options': [('A', 'Apply for part-time job'), ('B', 'Join the workshop')],
           'outcomes': {'A': (7000, -10, -2, -3), 'B': (0, 10, 2, 3)}},

    'BA': {'options': [('A', 'Accept'), ('B', 'Decline')],
           'outcomes': {'A': (0, 15, 0, 5), 'B': (5000, -15, -3, 2)}},

    'BB': {'options': [('A', 'Invest in gym membership'), ('B', 'Focus on Academics')],
           'outcomes': {'A': (-5000, 0, 5, 5), 'B': (0, 3, -3, -5)}},

    'BC': {'options': [('A', 'Attend event'), ('B', 'Skip event')],
           'outcomes': {'A': (-5000, 7, -2, 5), 'B': (0, 3, 2, -5)}},

    'BD': {'options': [('A', 'Take summer internship'), ('B', 'Take summer vacation')],
           'outcomes': {'A': (7000, 7, 5, 5), 'B': (-5000, -7, 5, 5)}},
    
    'CA': {'options': [('A', 'Pay with your loan'), ('B', 'Prioritize studies')],
           'outcomes': {'A': (-15000, 10, 5, 15), 'B': (0, 5, -7, -10)}},

    'CB': {'options': [('A', 'Accept'), ('B', 'Decline')],
           'outcomes': {'A': (-85000, 15, 0, 5), 'B': (0, 5, 0, 5)}},

    'CC': {'options': [('A', 'Time on relationship'), ('B', 'Prioritize studies')],
           'outcomes': {'A': (-10000, -10, 5, 5), 'B': (0, 10, -5, -5)}},

    'CD': {'options': [('A', 'Invest savings'), ('B', 'Research')],
           'outcomes': {'A': (-30000, 15, -5, 5), 'B': (-5000, 5, -3, 3)}},
    
    'DA': {'options': [('A', 'Buy new laptop'), ('B', 'Stick with current laptop')],
           'outcomes': {'A': (-50000, 10, 0, 5), 'B': (0, 2, 0, -2)}},

    'DB': {'options': [('A', 'Attend'), ('B', 'Decline')],
           'outcomes': {'A': (-25000, 10, 5, 5), 'B': (10000, -10, -5, -5)}},

    'DC': {'options': [('A', 'Enroll to the course'), ('B', 'Self-study')],
           'outcomes': {'A': (-35000, 10, -5, 5), 'B': (0, 2, -2, -3)}},

    'DD': {'options': [('A', 'Purchase new regalia'), ('B', 'Rent a set of regalia')],
           'outcomes': {'A': (-15000, 0, 0, 5), 'B': (-7500, 0, 0, 2)}},
    # Add more scenarios as needed...
}

"""
Author: Lucas Roberts
Date: 2/27/22
Description: The player class for tracking balances and other game events
"""
from random import choice, randint


class Player:

    def __init__(self):
        self.age, self.job = Player.determine_job()
        self.balance = 0
        self.roth = 0
        self.savings = 0

    def get_new_income(self):
        if self.age >= 40:
            return "Expert Income"
        elif self.age >= 30:
            return "Intermediate Income"
        else:
            return "Entry Income"

    @staticmethod
    def determine_job():
        starting_age = [25, 30, 35, 40, 45]
        job_list = {1: {"Job Title": "Server/Waitress", "Entry Income": "35,000", "Intermediate Income":
                        "40,000", "Expert Income": "50,000"},
                    2: {"Job Title": "Manufacturer", "Entry Income": "35,000", "Intermediate Income": "45,000",
                        "Expert Income": "65,000"},
                    3: {"Job Title": "Software Engineer", "Entry Income": "55,000", "Intermediate Income": "100,000",
                        "Expert Income": "150,000"},
                    4: {"Job Title": "Accountant", "Entry Income": "45,000", "Intermediate Income": "55,000",
                        "Expert Income": "70,000"},
                    5: {"Job Title": "Doctor", "Entry Income": "75,000", "Intermediate Income": "100,000",
                        "Expert Income": "200,000"},
                    6: {"Job Title": "Teacher", "Entry Income": "40,000", "Intermediate Income": "50,000",
                        "Expert Income": "60,000"},
                    7: {"Job Title": "Mechanic", "Entry Income": "45,000", "Intermediate Income": "55,000",
                        "Expert Income": "75,000"},
                    8: {"Job Title": "Nurse", "Entry Income": "65,000", "Intermediate Income": "75,000",
                        "Expert Income": "85,000"},
                    9: {"Job Title": "Police Officer", "Entry Income": "45,000", "Intermediate Income": "55,000",
                        "Expert Income": "65,000"},
                    10: {"Job Title": "Truck Driver", "Entry Income": "50,000", "Intermediate Income": "60,000",
                         "Expert Income": "75,000"},
                    11: {"Job Title": "Therapist", "Entry Income": "35,000", "Intermediate Income": "40,000",
                         "Expert Income": "50,000"},
                    12: {"Job Title": "Environmentalist", "Entry Income": "35,000", "Intermediate Income": "45,000",
                         "Expert Income": "55,000"},
                    13: {"Job Title": "CEO", "Entry Income": "100,000", "Intermediate Income": "200,000",
                         "Expert Income": "300,000"},
                    14: {"Job Title": "Lawyer", "Entry Income": "65,000", "Intermediate Income": "80,000",
                         "Expert Income": "95,000"},
                    15: {"Job Title": "Sales Person", "Entry Income": "40,000", "Intermediate Income": "70,000",
                         "Expert Income": "85,000"}
                    }

        player_age = choice(starting_age)
        # Had to use randint in this situation because choice() was throwing a Key error due to nested dic
        player_job = job_list[randint(1, 15)]
        return player_age, player_job

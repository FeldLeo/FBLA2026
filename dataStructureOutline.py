decisions = [
    {
        "event": "Customer suggests new menu item.",  # description of what happens today
        "choice1": {
            "text": "Add it to the menu.",  # label for the first button
            "effects": {
                "money": 0,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": +14 # change in customer satisfaction
            }
        },

        "choice2": {
            "text": "Ignore the suggestion.",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -10
            }
        }
    },
    {
        "event": "Customer posts positive review online.",  # description of what happens today

        "choice1": {
            "text": "Okay.",  # label for the first button
            "effects": {
                "money": 0,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": +9 # change in customer satisfaction
            }
        }
    },
    {
        "event": "A customer can't pay for their food.",  # description of what happens today

        "choice1": {
            "text": "Make him work off his meal.",  # label for the first button
            "effects": {
                "money": +12,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": -13 # change in customer satisfaction
            }
        },

        "choice2": {
            "text": "Let it slide.",  # label for the second button
            "effects": {
                "money": -7,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        }
    },
    {
        "event": "Employee is late for work.",  # description of what happens today

        "choice1": {
            "text": "Punish him.",  # label for the first button
            "effects": {
                "money": 0,              # change in money (can be + or -)
                "employee_happiness": -10, # change in employee happiness
                "customer_satisfaction": 0 # change in customer satisfaction
            }
        },

        "choice2": {
            "text": "Let it slide.",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": +9,
                "customer_satisfaction": -6
            }
        }
    },
    {
        "event": "New health codes enforced.",  # description of what happens today

        "choice1": {
            "text": "Pay to follow regulations.",  # label for the first button
            "effects": {
                "money": -15,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": 0 # change in customer satisfaction
            }
        },

        "choice2": {
            "text": "Ignore it.",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -13
            }
        }
    },
    {
        "event": "Rival business steals customers.",  # description of what happens today

        "choice1": {
            "text": "Run a new advertising campaign.",  # label for the first button
            "effects": {
                "money": -14,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": +10 # change in customer satisfaction
            }
        },

        "choice2": {
            "text": "Ignore the competition",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -12
            }
        }
    },
    {
        "event": "Employee gets injured outside of work.",  # description of what happens today

        "choice1": {
            "text": "Hire another employee.",  # label for the first button
            "effects": {
                "money": -12,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": 0 # change in customer satisfaction
            }
        },

        "choice2": {
            "text": "Wait until he returns.",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -10
            }
        }
    },
    {
        "event": "Employee requests a raise.",  # description of what happens today
        "choice1": {
            "text": "Give raise.",  # label for the first button
            "effects": {
                "money": -13,              # change in money (can be + or -)
                "employee_happiness": +15, # change in employee happiness
                "customer_satisfaction": 0 # change in customer satisfaction
            }
        },
        "choice2": {
            "text": "Deny raise.",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": -11,
                "customer_satisfaction": 0
            }
        }
    },
    {
        "event": "Customer accidentally breaks soda machine.",  # description of what happens today
        "choice1": {
            "text": "Make them pay for it.",  # label for the first button
            "effects": {
                "money": 0,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": -9 # change in customer satisfaction
            }
        },
        "choice2": {
            "text": "Forgive them, foot the bill.",  # label for the second button
            "effects": {
                "money": -12,
                "employee_happiness": 0,
                "customer_satisfaction": +6
            }
        }
    },
    {
        "event": "",  # description of what happens today
        "choice1": {
            "text": "",  # label for the first button
            "effects": {
                "money": 0,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": 0 # change in customer satisfaction
            }
        },
        "choice2": {
            "text": "",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        }
    },
    {
        "event": "",  # description of what happens today
        "choice1": {
            "text": "",  # label for the first button
            "effects": {
                "money": 0,              # change in money (can be + or -)
                "employee_happiness": 0, # change in employee happiness
                "customer_satisfaction": 0 # change in customer satisfaction
            }
        },
        "choice2": {
            "text": "",  # label for the second button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        }
    },
    # ... More decisions go here ...
]

"""
 decisions: a list that holds all events (surrounded by [ ])

 Each event: a dictionary (surrounded by { })

 event: a string describing the scenario

 choice1 / choice2: two dictionaries, one for each possible decision

 text: what we display on the button in html

 effects: another dictionary that holds how much each variable should change
"""

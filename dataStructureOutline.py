decisions = [
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


# decisions: a list that holds all events (surrounded by [ ])

# Each event: a dictionary (surrounded by { })

# event: a string describing the scenario

# choice1 / choice2: two dictionaries, one for each possible decision

# text: what we display on the button in html

# effects: another dictionary that holds how much each variable should change

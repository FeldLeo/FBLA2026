from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

day = 1
money = 50
customer_satisfaction = 50
employee_happiness=50

decisions = [
    {
        "event": "An employee asks for a raise.",
        "choice1": {
            "text": "Give raise",
            "effects": {
                "money": -10,
                "employee_happiness": +15,
                "customer_satisfaction": 0
            }
        },
        "choice2": {
            "text": "Deny raise",
            "effects": {
                "money": 0,
                "employee_happiness": -10,
                "customer_satisfaction": 0
            }
        }
    },

    {
        "event": "Customer is upset about a rude employee.",
        "choice1": {
            "text": "Ignore complaint",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -10
            }
        },
        "choice2": {
            "text": "Fire employee",
            "effects": {
                "money": 0,
                "employee_happiness": -10,
                "customer_satisfaction": 0
            }
    }
    {
        "event": "Hire more employees for better efficiency?",
        "choice1": {
            "text": "Hire Employees"
            "effects": {
                "money": -14,
                "employee_happiness": 0,
                "customer_satisfaction": +11
                }
            },
        "choice2": {
            "text": "Don't hire employees"
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": 0
                }
            }
    },
    {
        "event": "Charity requests fundraiser where all proceeds on Tuesday night goes to charity.",
        "choice1": {
            "text": "Accept fundraiser", 
            "effects": {
                "money": -10,              
                "employee_happiness": 0, 
                "customer_satisfaction": +14
            }
        },
        "choice2": {
            "text": "Decline fundraiser",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -8
            }
        }
    },
    {
        "event": "Ice cream machine breaks.",
        "choice1": {
            "text": "Buy new machine", 
            "effects": {
                "money": -11,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        },
        "choice2": {
            "text": "Wait for more money and go without a machine for now",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -12
            }
        }
    },
    {
        "event": "Owner wants to meet with you, but it conflicts with an employee’s birthday party.", 
        "choice1": { 
            "text": "Meet with owner",  
            "effects": { 
                "money": +15, 
                "employee_happiness": -8, 
                "customer_satisfaction": 0 
            } 
        }, 
        "choice2": { 
            "text": "Attend employee party", 
            "effects": { 
                "money": 0, 
                "employee_happiness": +11, 
                "customer_satisfaction": 0 
            } 
        } 
    }, 
        {
        "event": "Good employee gets big tip.", 
        "choice1": { 
            "text": "Praise employee",  
            "effects": { 
                "money": 0, 
                "employee_happiness": +9, 
                "customer_satisfaction": 0 
            } 
        }, 
        "choice2": { 
            "text": "Give employee a raise", 
            "effects": { 
                "money": -6, 
                "employee_happiness": +15, 
                "customer_satisfaction": 0 
            } 
        } 
    }, 
        {
        "event": "Customer accidentally breaks soda machine.", 
        "choice1": { 
            "text": "Demand customer pays for it",  
            "effects": { 
                "money": 0, 
                "employee_happiness": 0, 
                "customer_satisfaction": -9 
            } 
        }, 
        "choice2": { 
            "text": "Forgive customer and foot the bill", 
            "effects": { 
                "money": -12, 
                "employee_happiness": 0, 
                "customer_satisfaction": +6 
            } 
        } 
    },
        {
        "event": "Customer suggests new menu item.",
        "choice1": {
            "text": "Add it to the menu.",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": +14
            }
        },

        "choice2": {
            "text": "Ignore the suggestion.",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -10
            }
        }
    },
    {
        "event": "Customer posts positive review online.",

        "choice1": {
            "text": "Okay.",  # label for the first button
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": +9
            }
        }
    },
    {
        "event": "A customer can't pay for their food.",

        "choice1": {
            "text": "Make him work off his meal.",
            "effects": {
                "money": +12,
                "employee_happiness": 0,
                "customer_satisfaction": -13
            }
        },

        "choice2": {
            "text": "Let it slide.",
            "effects": {
                "money": -7,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        }
    },
    {
        "event": "Employee is late for work.",

        "choice1": {
            "text": "Punish him.",
            "effects": {
                "money": 0,
                "employee_happiness": -10,
                "customer_satisfaction": 0
            }
        },

        "choice2": {
            "text": "Let it slide.",
            "effects": {
                "money": 0,
                "employee_happiness": +9,
                "customer_satisfaction": -6
            }
        }
    },
    {
        "event": "New health codes enforced.",

        "choice1": {
            "text": "Pay to follow regulations.",
            "effects": {
                "money": -15,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        },

        "choice2": {
            "text": "Ignore it.",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -13
            }
        }
    },
    {
        "event": "Rival business steals customers.",

        "choice1": {
            "text": "Run a new advertising campaign.",
            "effects": {
                "money": -14,
                "employee_happiness": 0,
                "customer_satisfaction": +10
            }
        },

        "choice2": {
            "text": "Ignore the competition",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -12
            }
        }
    },
    {
        "event": "Employee gets injured outside of work.",
        "choice1": {
            "text": "Hire another employee.",
            "effects": {
                "money": -12,
                "employee_happiness": 0,
                "customer_satisfaction": 0
            }
        },

        "choice2": {
            "text": "Wait until he returns.",
            "effects": {
                "money": 0,
                "employee_happiness": 0,
                "customer_satisfaction": -10
            }
        }
    }          
]

current_event = random.choice(decisions)




@app.route('/')
def home():
    print(">>> Rendering index.html")
    return render_template(
        'index.html',
        day=day,
        money=money,
        employee_happiness=employee_happiness,
        customer_satisfaction=customer_satisfaction,
        event=current_event["event"],
        choice1=current_event["choice1"]["text"],
        choice2=current_event["choice2"]["text"],
    )

@app.route('/action/<choice>', methods=['POST'])
def action(choice):
    global day, money, employee_happiness, customer_satisfaction, current_event

    effects = current_event[choice]["effects"]

    # Apply effects
    money += effects["money"]
    employee_happiness += effects["employee_happiness"]
    customer_satisfaction += effects["customer_satisfaction"]

   
    money = max(0, min(money, 100)) # keeps values from going below 0 or over 100
    customer_satisfaction = max(0, min(customer_satisfaction, 100))
    employee_happiness = max(0, min(employee_happiness, 100))

    return redirect(url_for('home'))  # reloads home page with updated values
    
    day += 1
    current_event = random.choice(decisions)

if __name__ == '__main__':
    app.run(debug=True)




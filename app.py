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

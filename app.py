from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

day = 1
money = 50
customer_satisfaction = 50
employee_happiness = 50


@app.route('/')
def home():
    print(">>> Rendering NEW index.html")
    return render_template(
        'index.html', 
        day=day,
        money=money,
        customer_satisfaction=customer_satisfaction
        employee_happiness=employee_happiness
    )

@app.route('/action', methods=['POST'])
def action():
    global day, money, customer_satisfaction, employee  # allows modifying variables

    # Example: clicking the button decreases money by 10, increases happiness by 5
    money -= 10
    employee_happiness += 5
    day += 1

   
    money = max(0, min(money, 100)) # keeps values from going below 0 or over 100
    customer_satisfaction = max(0, min(customer_satisfaction, 100))
    employee_happiness = max(0, min(employee_happiness, 100))


    return redirect(url_for('home'))  # reloads home page with updated values

if __name__ == '__main__':

    app.run(debug=True)

name = input("Enter the name of your company: ") + "™"
def menu():
    print("\nWelcome to the Truck game! You are a truck manager and your job is to direct trucks where they need to go without going broke!")
    print("\nLet's get your company, " + name + ", started!")
    start_game()

def start_game():
    print("\nGame started")
    print("\nType 1 for instructions on how to play if you haven't played before")
    print("Type 2 to continue if you're a delivery truck pro")
    choice = input("Type 1 or 2: ")
    if choice == "1":
        help()
    elif choice == "2":
        first_route()
    else:
        print("Please type either 1 or 2")
        start_game()
def help():
    print("")
money = 1000.00
day = 1
time = 24
fuel = 0
smallTrucks = 1
bigTrucks = 0
smallTrucksMPG = 7
smallTrucksTank = 150
gasRate = 3.5
routes = {
    
        "Louisville": [
            {"to": "Cincinnati","description": "Cincinnati Celery Co. needs a truckload of celery.", "distance": 100, "due": 24, "size": "small", "cost": (100 / smallTrucksMPG) * gasRate, "payout": 100},
            {"to": "Indianapolis", "description": "Indianapolis Ink, Inc. needs a truckload of ballpoint pens.", "distance": 124, "due": 24, "size": "small", "cost": (124 / smallTrucksMPG) * gasRate, "payout": 112},
            {"to": "Saint Louis", "description": "Saint Louis Logging Service needs a truckload of chainsaws", "distance": 250, "due": 24, "size": "small", "cost": (250 / smallTrucksMPG) * gasRate, "payout": 230}, 
        ]
        "Cincinnati": []
        "Indianapolis": []
        "Saint Louis": []

    
}
def first_route():
    print("\nCompany Name: ", name)
    print("Money: ", money)
    print("Time: ", time, ":00")
    print("Total Trucks:", smallTrucks + bigTrucks)



menu()

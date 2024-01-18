MENU = {
    "royal": {
        "ingredients": {
            "water": 50,
            "soda": 18,
            "drink": 50,
        },
        "cost": 650,
    },
    "old monk": {
        "ingredients": {
            "water": 200,
            "soda": 150,
            "drink": 24,
        },
        "cost": 1500,
    },
    "boom91": {
        "ingredients": {
            "water": 250,
            "drink": 8,
            "soda": 24,
        },
        "cost": 190,
    },
    "vodka": {
        "ingredients": {
            "water": 50,
            "drink": 80,
            "soda": 24,
        },
        "cost": 340,
    },
    "desi": {
        "ingredients": {
            "water": 10,
            "drink": 120,
            "soda": 0,
        },
        "cost": 80,
    },
    "wine": {
        "ingredients": {
            "water": 0,
            "drink": 80,
            "soda": 0,
        },
        "cost": 2000,
    }
}

profit = 0
resources = {
    "water": 300,
    "soda": 200,
    "drink": 900,
}

class Report:
    def __init__(self):
        self.menu = MENU
        self.resource = resources
        self.profit = profit

class Order(Report):
    def __init__(self, data):
        Report.__init__(self)
        self.data = data

    def resources(self):
        if (
            self.menu[self.data]["ingredients"]["water"] < self.resource["water"]
            and self.menu[self.data]["ingredients"]["soda"] < self.resource["soda"]
            and self.menu[self.data]["ingredients"]["drink"] < self.resource["drink"]
        ):
            print("Insert Money")
            # Deduct resources
            self.resource["water"] -= self.menu[self.data]["ingredients"]["water"]
            self.resource["soda"] -= self.menu[self.data]["ingredients"]["soda"]
            self.resource["drink"] -= self.menu[self.data]["ingredients"]["drink"]

        if self.menu[self.data]["ingredients"]["water"] > self.resource["water"]:
            print(f"Sorry there is not enough water!!!")
        elif self.menu[self.data]["ingredients"]["soda"] > self.resource["soda"]:
            print(f"Sorry there is not enough soda !!!")
        elif self.menu[self.data]["ingredients"]["drink"] > self.resource["drink"]:
            print(f"Sorry there is not enough drink!!!")
    
    def report(self):
        print("Current Resource Status:")
        print(f"Water: {self.resource['water']}ml")
        print(f"Soda: {self.resource['soda']}ml")
        print(f"Drink: {self.resource['drink']}ml")
        print(f"Money: ${self.profit:.2f}")

class Money(Order):
    def __init__(self, data, money):
        Order.__init__(self, data)
        self.money = money
        self.c = 0

    def transaction_successfully(self):
        remaining = self.money - self.menu[self.data]["cost"]
        self.profit += self.menu[self.data]["cost"]
        if self.menu[self.data]["cost"] == self.money:
            print(f"Enjoy your {self.data.capitalize()}")
        elif self.menu[self.data]["cost"] > self.money:
            print("Not enough money")
        elif self.menu[self.data]["cost"] < self.money:
            print(f"Enjoy your {self.data.capitalize()} and keep your change for Chakhna: ${remaining:.2f}")

class NotesInput(Money):
    def __init__(self, data, notes):
        Money.__init__(self, data, 0)
        self.notes = notes

    def process_notes(self):
        total_money = 0
        for note_value, note_count in self.notes.items():
            total_money += int(note_value) * note_count
        self.money = total_money
        self.transaction_successfully()

i = 1
while i <= 100:
    print("""What would you like from Wine Shop?
          ------royal🍾:650rs---------
          ------Old Monk🥂:650rs------
          ------Boom91🍺:650rs--------
          ------Vodka🍹:650rs---------
          ------Desi🍶:650rs----------
          ------wine🍸:650rs----------""")
    data1 = input("Enter your order: ")
    data = data1.lower()
    obj = Order(data)
    
    if data in ["royal", "old monk", "boom91", "vodka", "desi", "wine"]:
        obj.resources()
        notes = {
            50: int(input("Enter the quantity of 50 rs notes: ")),
            100: int(input("Enter the quantity of 100 rs notes: ")),
            200: int(input("Enter the quantity of 200 rs notes: ")),
            500: int(input("Enter the quantity of 500 rs notes: "))
        }
        obj2 = NotesInput(data, notes)
        obj2.process_notes()
    elif data == "report":
        obj.report()
    else:
        print("Wrong Order...?")

    continue_order = input("Do you want to continue? (yes/no): ").lower()
    if continue_order != 'yes':
        print("Thank you for visiting Thekka. Have a great day!")
        break

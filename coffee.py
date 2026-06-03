class coffee():
    def __init__(self,name,milk,sugar,water,price):
        self.name = name
        self.milk = milk
        self.sugar = sugar 
        self.water = water
        self.price = price
        
    
class capicinno(coffee):
        def __init__(self):
            super().__init__(
            name="Cappuccino",
            milk=50,
            water=30,
            sugar=10,
            price=150
        )
            

class latte(coffee):
        def __init__(self):
            super().__init__(
            name="latte",
            milk=70,
            water=40,
            sugar=10,
            price=180
        )

class espresso(coffee):
        def __init__(self):
            super().__init__(
            name="Cappuccino",
            milk=20,
            water=60,
            sugar=5,
            price=120
        )
            
class inventory():
    def __init__(self,milk,water,sugar):
        self.milk = milk
        self.sugar = sugar 
        self.water = water
     
    def check_resources(self, coffee):
        return (
            self.milk >= coffee.milk and
            self.water >= coffee.water and
            self.sugar >= coffee.sugar
        )
        
    def consume(self, coffee):
        self.milk -= coffee.milk
        self.water -= coffee.water
        self.sugar -= coffee.sugar
        
           
    def storage(self):
        print(f"total amount of milk in machine : {self.milk} ml")
        print(f"total amount of water in machine : {self.water} ml")
        print(f"total amount of sugar in machine : {self.sugar} gm")
        
    
    def refill(self):
        milk = int(input("enter amount of addded milk : "))
        water = int(input("enter amount of addded water : "))
        sugar = int(input("enter amount of addded sugar : "))
        
        ## new volume
        self.milk = self.milk + milk
        self.water = self.water + water
        self.sugar = self.sugar + sugar
        
        
class coffee_machine(inventory):
    def __init__(self, milk, water, sugar):
        super().__init__(milk, water, sugar)

    def make_coffee(self, coffee):

        if not self.check_resources(coffee):
            print("\nNot enough ingredients!")
            return

        self.consume(coffee)

        print("\nPreparing Coffee...")
        print(f"{coffee.name} Ready ☕")
        print(f"Please Pay ₹{coffee.price}")
        
    def start(self):

        while True:
            user_input =input("""
    Hi which coffee you want??
    1. Press 1 for capicinno
    2. Press 2 for latte
    3. Press 3 for esperreso
    4. Press 4 for storage 
    5. press 5 for refill
    6. Anything else to exit
    """)
            
            if user_input == "1":
                self.make_coffee(capicinno())

            elif user_input == "2":
                self.make_coffee(latte())

            elif user_input == "3":
                self.make_coffee(espresso())

            elif user_input == "4":
                self.storage()

            elif user_input == "5":
                self.refill()

            elif user_input == "6":
                print("Thank You!")
                break

            else:
                print("Invalid Choice")
            
        
        

    
        
machine = coffee_machine(
    milk=1000,
    water=1000,
    sugar=500
)

machine.start()
    
        
        

    
        
class Car:
    def __init__(self, colour, speed=0):           # Fixed: __init__ (double underscore)
        self.color = colour
        self.speed = speed
        self.engine_running = False

    def start_engine(self):
        self.engine_running = True
        print(f"{CYAN}{self.color} Initializing Car engine starting............. "
              f"Vroooooooooom. Vroooom, Vrooooooooommmmmm!!{RESET}")

    def drive(self, new_speed):
        if self.engine_running:
            self.speed = new_speed
            print(f"{GREEN}Driving {self.color} car at {new_speed} mph.{RESET}")
        else:
            print(f"{RED}Engine's off bro. Start it first and hear the rooooarr!{RESET}")

    def honk(self):
        print(f"{YELLOW}Beeeeeeeeep!{RESET}")

    def brake(self):
        print(f"{RED}Braking... Screeeech!{RESET}")

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Now make real cars (objects)
my_car = Car("AUDI TTRS", 0)          # Audi TTRS parked
friend_car = Car("blue", 60)    

my_car.start_engine()           # red car starts
my_car.drive(125)                # red car speeds up
friend_car.honk()               # blue car beeps

print("\n--- <><> Now the AUDI R8 <><> ---")

class SportsCar(Car):
    def __init__(self, colour, speed=0):
        super().__init__(colour, speed) 
        self.turbo=False

    def boost(self):
        if self.engine_running:
            self.turbo = True
            self.speed *= 2
            print(f"\n{RED}<<<<<<<<< BOOOSTT ACTIVATEDDD ROARRRRRR >>>>>>>>>{RESET}\n")
        else:
            print(f"{RED}Can't boost! Engine is off.{RESET}")

my_ride = SportsCar("Audi R8", 60)
my_ride.start_engine()
my_ride.drive(150)
my_ride.boost()
my_ride.drive(700)





class Car:
    def __init__(self, colour, speed=0):     
        self.colour = colour
        self.speed = speed
        self.engine_running = False
    # Initializes car with colour, speed, engine off

    def start_engine(self):
        self.engine_running = True
        print(f"{CYAN}{self.colour} Initializing Car engine starting............. "
              f"Vroooooooooom. Vroooom, Vrooooooooommmmmm!!{RESET}")
    # Engine starts 

    def drive(self, new_speed):
        if self.engine_running:
            self.speed = new_speed
            print(f"{GREEN}Driving {self.colour} car at {new_speed} mph.{RESET}")
        else:
            print(f"{RED}Engine's off bro. Start it first and hear the rooooarr!{RESET}")
    # Drives at given speed if engine on

    def honk(self):
        print(f"{YELLOW}Beeeeeeeeep!{RESET}")
    # Simple horn beep

    def brake(self):
        print(f"{RED}Braking... Screeech!{RESET}")
    # Brake sound effect

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
# ANSI starts printing colours to the texts

# Objects
my_car = Car("AUDI TTRS", 0)          # Audi TTRS parked
friend_car = Car("blue", 60)    

my_car.start_engine()           # Starts the TTRS
my_car.drive(125)               # Drives at 125 mph
my_car.honk()               # TTRS beeps

print("\n--- <><> Now the AUDI R8 <><> ---")

class SportsCar(Car):
    def __init__(self, colour, speed=0):
        super().__init__(colour, speed)  # Calls parent's init for color/speed/engine, Super() keeps it simple by not repeating parent's init from Class car
        self.turbo = False
    # Inherits from Car, adds turbo flag

    def boost(self):
        if self.engine_running:
            self.turbo = True
            self.speed *= 2 # multiplying by 2 
            print(f"\n{RED}<<<<<<<<< BOOOSTT ACTIVATEDDD ROARRRRRR >>>>>>>>>{RESET}\n")
        else:
            print(f"{RED}Can't boost! Engine is off.{RESET}")
    # Doubles speed with turbo if engine running

my_ride = SportsCar("Audi R8", 60)
my_ride.start_engine()
my_ride.drive(125)
my_ride.boost()
my_ride.drive(204)  # Now at 204 mph 





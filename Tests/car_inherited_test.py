from car import SportsCar, Car

def test_inheritance():
    # Test inheritance: SportsCar gets Car's state/methods + adds turbo
    my_ride = SportsCar("Audi R8", 60)  # Create SportsCar (calls super().__init__)
    my_ride.start_engine()               # Inherited method from Car
    assert my_ride.engine_running        # Verifies inherited attr True after start
    assert hasattr(my_ride, "turbo")     # SportsCar adds 'turbo' attr
    assert not hasattr(Car("Audi R8", 60), "turbo")  # Base Car lacks turbo

def test_boost():
    # Test boost doubles speed + sets turbo=True
    my_ride = SportsCar("Audi R8", 60)   # Initial speed=60
    old_speed = my_ride.speed            # Capture before (60)
    my_ride.start_engine()               # Need engine for boost (if check added)
    my_ride.boost()                      # Doubles speed, sets turbo=True
    assert my_ride.speed == old_speed * 2  # Verifies 120

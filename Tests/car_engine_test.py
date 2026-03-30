from car import Car

def test_start_engine():
    my_car = Car("AUDI TTRS", 0)
    my_car.start_engine()
    assert my_car.engine_running == True



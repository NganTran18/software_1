class Car():
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0
    def info(self):
        print("Car properties")
        print(f"Registration number: {self.number}")
        print(f"Speed:{new_car.max_speed}")
        print(f"Current speed:{self.current_speed}")
        print(f"Distance:{new_car.distance}")

    def accelerate(self, change_speed):
        new_speed = self.current_speed + change_speed
        if new_speed < 0:
            self.current_speed = 0
        elif new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, hours_number):
        self.distance += self.current_speed * hours_number

# information
new_car = Car("ABC-123", 142)
new_car.info()
# accelerate
new_car.accelerate(30)
print(f"Current speed: {new_car.current_speed}")
new_car.accelerate(70)
print(f"New speed: {new_car.current_speed}")
new_car.accelerate(50)
print(f"New speed: {new_car.current_speed}")
new_car.accelerate(-200)
print(f"Brake & final speed: {new_car.current_speed}")
# drive
new_car.drive(1.5)
print(f"Travelled distance: {new_car.distance}")
#


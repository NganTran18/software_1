class Car():
    def __init__(self, number, max_speed):
        self.number = number
        self.max_speed = max_speed
        self.kilometer = 0
    def drive(self, speed, hours):
        if speed <= self.max_speed:
            self.kilometer += hours * speed
        else:
            self.kilometer += hours * self.max_speed
            print(f'speed is {speed}, max speed is {self.max_speed}.')

class ElectricCar(Car):
    def __init__(self, number, max_speed, battery):
        super().__init__(number, max_speed)
        self.battery = battery
    def info(self):
        print(f'number: {self.number}, max_speed: {self.max_speed}km/h, battery: {self.battery}kWh')
class Gasoline(Car):
    def __init__(self, number, max_speed, tank):
        super().__init__(number, max_speed)
        self.tank = tank
    def info(self):
        print(f'number: {self.number}, max_speed: {self.max_speed}km/h, tank: {self.tank}l')
elecar = ElectricCar("ABC-15", 180, 52.5)
gasocar = Gasoline("ACD-123",165, 32.3)
elecar.info()
gasocar.info()
#select speed for 3 hours
elecar_speed = 100
gasocar_speed = 100

elecar.drive(elecar_speed, 3)
gasocar.drive(elecar_speed, 3)

print(f'kilometer of electric car: {elecar.kilometer}')
print(f'kilometer of gasoline car: {gasocar.kilometer}')


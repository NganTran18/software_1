class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.floor = self.bottom

    def floor_up(self):
        if self.floor < self.top:
            self.floor += 1
            print("The elevator is on", self.floor, "floor")
        else:
            print("you are in top floor")

    def floor_down(self):
        if self.floor > self.bottom:
            self.floor -= 1
            print("the elevator is on", self.floor, "floor")
        else:
            print("you are in bottom floor")

    def go_to_floor(self, main_floor):
        self.main_floor = main_floor
        if self.main_floor > self.floor:
            self.floor_up()
        elif self.main_floor < self.main_floor:
            self.floor_down()
        else:
            print("invalid")


class Building:
    def __init__(self, bottom, top, num_elevator):
        self.bottom = bottom
        self.top = top
        self.num_elevator = num_elevator
        self.elevators = [Elevator(self.bottom, self.top) for _ in range(num_elevator)]

    def run_elevator(self, number, destination):
        self.number = number
        self.destination = destination

    def fire_alarm(self):
        print("Fire alam!!!")
        for i in self.elevators:
            i.go_to_floor(self.bottom)

h = Elevator(1, 10 )
h.go_to_floor(5)
h.go_to_floor(1)
fire = Building(5, 1, 3)
fire.run_elevator(0, 5)
fire.fire_alarm()
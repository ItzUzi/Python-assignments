import math


class Bicycle:
    def __init__(self, gear, speed):
        self.gear = gear
        self.speed = speed

    def apply_brake(self, decrement):
        self.speed -= decrement

    def speed_up(self, increment):
        self.speed += increment

    def up_hill(self, incline):
        self.speed *= (.7**(incline*.25))

    def __str__(self):
        return "No of gears are %d \n" \
               "speed of bicycle is %d" % (self.gear, self.speed)


class MountainBike(Bicycle):
    def __init__(self, gear, speed, seat_height):
        super().__init__(gear, speed)
        self.seat_height = seat_height

    def set_height(self, new_value):
        self.seat_height = new_value

    def up_hill(self, incline):
        self.speed *= (.9**(incline*.25))

    def jump_height(self, ramp_incline):
        degrees = ramp_incline * (math.pi/180)
        return (self.speed*math.sin(degrees))**2/(2*9.8)

    def __str__(self):
        return super().__str__() + "\nseat height is %d" \
               % self.seat_height


def main():
    mb = MountainBike(3, 100, 25)
    bike = Bicycle(3, 100)
    print("Base bike and mountain bike")
    print(bike)
    print(mb, end='\n\n')
    print("Testing inheritance of function")
    mb.apply_brake(20)
    print(mb, end='\n\n')
    mb.speed_up(20)     # resets to base values
    print("Testing overloading functions")
    bike.up_hill(45)
    mb.up_hill(45)
    print(bike)
    print(mb, end='\n\n')
    print("Testing mb own function")
    print("Jump height is", mb.jump_height(45), end='\n\n' )


if __name__ == '__main__':
    main()

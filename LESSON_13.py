# 1. Create add method to add two countries together.
# This method should create another country object with the name of the
# two countries combined and the population of the two countries added together.

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add_met(self, otherCountry):
        return Country(self.name + ' ' + otherCountry.name, self.population + otherCountry.population)
    
bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia.add_met(herzegovina)
print(bosnia_herzegovina.name, bosnia_herzegovina.population)

# 2. Implement the previous method with a magic method

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
    
    def __add__(self, otherCountry):
        return Country(self.name + otherCountry.name, self.population + otherCountry.population)

bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)
bosnia_herzegovina = bosnia + herzegovina
print(bosnia_herzegovina.name, bosnia_herzegovina.population)

# 3. Create a Car class with the following attributes: brand, model,
# year, and speed. The Car class should have the following methods:
# accelerate, brake and display_speed. The accelerate method should
# increase the speed by 5, and the brake method should decrease the
# speed by 5. Remember that the speed cannot be negative.

class Car:
    def __init__(self, brand: str, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
    def accelerate(self):
        self.speed += 5
    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0
    def display_speed(self):
        print ('Current speed: ', self.speed)
    
mazda = Car('Mazda', 's200j', 2009, 8)

mazda.display_speed()

mazda.accelerate()
mazda.display_speed()

mazda.accelerate()
mazda.display_speed()

mazda.brake()
mazda.display_speed()

mazda.brake()
mazda.display_speed()

# 4. (Optional) Create a Robot class with the following attributes: orientation (left, right, up, down), position_x, position_y.
# The Robot class should have the following methods: move, turn, and display_position. The move method should take a number of steps and move
# the robot in the direction it is currently facing.
# The turn method should take a direction (left or right) and turn the robot in that direction.
# The display_position method should print the current position of the robot.

class Robot:
    def __init__(self, orientation, position_x, position_y):
        self.orientation = orientation
        self.position_x = position_x
        self.position_y = position_y

    def move(self, step):
        if self.orientation == "up":
            self.position_y += step
        elif self.orientation == "down":
            self.position_y -= step
        elif self.orientation == "left":
            self.position_x -= step
        elif self.orientation == "right":
            self.position_x += step

    def turn(self, direct):
        self.orientation = direct

    def display_position(self):
        print(f"Current position: {self.position_x}, {self.position_y}")

robot = Robot("up", 5, 8)
robot.display_position()

robot.move(3)
robot.display_position()

robot.turn("down")
robot.move(7)
robot.display_position()

robot.turn("left")
robot.move(5)
robot.display_position()
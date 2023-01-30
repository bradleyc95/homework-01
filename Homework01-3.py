# Bradley Cox - Homework 01, Problem 3
# 01/31/2023

# function to calculate and print the momentum of an object based on its mass and velocity
def momentum(mass, velocity):
    momentum = mass * velocity
    print("Mass: " + str(mass))
    print("Velocity: " + str(velocity))
    print("The object's momentum is " + str(momentum))

# attempt to cast user input to floats and pass them into the momentum function
try:
    mass = float(input("Enter the object's mass: "))
    velocity = float(input("Enter the object's velocity: "))
    momentum(mass, velocity)
# throw error if unable to cast
except Exception:
    print("Error, mass and velocity must be numbers.")
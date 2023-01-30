# Bradley Cox - Homework 01, Problem 1
# 01/31/2023

# calculate the total price based on number of new videos and number of old videos
def calcPrice(new, old):
    total = 0
    # verify that inputs are integers
    if type(new) == int:
        for i in range(new):
            total += 3
        for j in range(old):
            total += 2
        print("The total cost is $" + str(total))
    # if inputs are not integers, throw error
    else:
        print("Unable to calculate total.")

# prompt user to enter number of videos they would like to purchase
def prompt():
    print("Welcome to Five Star Retro Video!")

    new = input("Enter the number of new videos: ")
    old = input("Enter the number of oldies: ")

    # attempt to cast new and old to ints, if this is not possible, throw error and return None
    try:
        new = int(new)
        old = int(old)
    except Exception:
        print("Error, input must be a whole number.")
        return (None, None)

    return (new, old)

new, old = prompt()
calcPrice(new, old)
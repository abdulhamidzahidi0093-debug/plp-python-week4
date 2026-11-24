# Week 4 Assignment - My First Toolbox

# This function doubles a number.
def double(number):
    return number * 2


# This function checks whether a learner has passed.
def is_pass(score):
    return score >= 50


# This function greets someone using a default greeting.
def greet(name, greeting="Hello"):
    return greeting + ", " + name + "!"


# Testing all three functions.
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))

# calculator

class Calculator:
    def __init__(self):
        pass

    # main math operations
    def add (self, num1, num2):
        return num1 + num2
    def subtract (self, num1, num2):
        return num1 - num2
    def multiply (self, num1, num2):
        return num1 * num2
    def divide (self, num1, num2):
        return num1 / num2 
    
    def run_calculator(self):
        try:
            # ask user for an operation
            operation = input("choose an operation (+, -, *, /): ")
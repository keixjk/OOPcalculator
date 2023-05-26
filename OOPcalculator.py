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
            # ask user for the first number
            num1 = float(input("enter the first number: "))
            # ask user for the second number
            num2 = float(input("enter the second number: "))

            # solve the input operation and numbers
            if operation == "+":
                result = self.add(num1, num2)
            if operation == "-":
                result = self.subtract(num1, num2)
            if operation == "*":
                result = self.multiply(num1, num2)
            if operation == "/":
                result = self.divide(num1, num2)
            else:
                print("Invalid operation")
                return
            
            # print result
            print("Result:", result)

            # ask user to try again or not
            choice = input("Do you want to try again? (yes/no): ")
            if choice.lower() == "yes":
                self.run_calculator
            else:
                print("Thank you!")

        # check for Value error
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            self.run_calculator()


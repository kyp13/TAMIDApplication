#Create a calculator

#retrieve input to begin program
ans = input("Welcome to the TAMID Calculator! "
      "Would you like to calculate something(y/n)?")

#calculator loop function
while ans == "y":
    #retrieve number and operator inputs
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operator = input("Please enter your function: ")
    #addition operator function
    if operator == "+":
        print("Your result was:", x+y, "!")
    #subtraction operator function
    if operator == "-":
        print("Your result was:", x-y, "!")
    #multiplication operator function
    if operator == "*":
        print("Your result was:", x*y, "!")
    #division operator function
    if operator == "/":
        #error correction for division
        if y == 0:
            print("Error: You cannot divide by zero!")
        elif operator == "/":
            print("Your result was:", x/y, "!")
    ans = input("Would you like to calculate something(y/n)")

print("Thanks for coming!")





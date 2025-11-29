# Getting numeric inputs
num1 = int(input("Enter first number: ")
num2 = int(input("Enter second number: "))

# Logic error is here intentionally
result = num1 - num2

print("The result is:", result)

import turtle

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.write("Answer: " + str(result), align="center", font=("Arial", 20))
t.hideturtle()

turtle.done()

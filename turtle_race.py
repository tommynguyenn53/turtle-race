import turtle
from turtle import Turtle, Screen
import random

# Initialize a flag to track if the race is active
is_race_on = False

# Set up the screen dimensions
screen = Screen()
screen.setup(width=500, height=400)

# Ask the user to place a bet on which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ").lower()

# Define the colors of the turtles
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# Starting y-coordinate for turtle placement
n = -80

# List to keep track of all turtle objects
all_turtles = []

# Create and position each turtle on the screen
for turtle_index in range(len(colours)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()  # Prevent the turtle from drawing while moving to starting position
    new_turtle.color(colours[turtle_index])  # Set the turtle's color
    new_turtle.goto(x=-230, y=n)  # Move the turtle to its starting line
    n += 35  # Space out turtles vertically
    all_turtles.append(new_turtle)  # Add the turtle to the list

# Start the race if the user placed a bet
if user_bet:
    is_race_on = True

# Main race loop
while is_race_on:

    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False  # Stop the race
            winning_colour = turtle.pencolor()  # Get the color of the winning turtle

            # Compare the winner with the user's bet
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")

        # Move the turtle forward by a random amount
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Close the screen when the user clicks on it
screen.exitonclick()

from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

is_race_on = False

orange = Turtle()
orange.color("orange")
orange.shape("turtle")
orange.penup()
orange.goto(x=-230, y=-100)

red = Turtle()
red.color("red")
red.shape("turtle")
red.penup()
red.goto(x=-230, y=-70)

green = Turtle()
green.color("green")
green.shape("turtle")
green.penup()
green.goto(x=-230, y=-40)

yellow = Turtle()
yellow.color("yellow")
yellow.shape("turtle")
yellow.penup()
yellow.goto(x=-230, y=-10)

blue = Turtle()
blue.color("blue")
blue.shape("turtle")
blue.penup()
blue.goto(x=-230, y=20)


purple = Turtle()
purple.color("purple")
purple.shape("turtle")
purple.penup()
purple.goto(x=-230, y=50)

bop_turtle = [red, orange, purple, blue, green, yellow]


line = Turtle()
line.penup()
line.goto(x=210, y=100)
line.pendown()
line.goto(x=210, y=-150)
line.hideturtle()

if user_bet:
    is_race_on = True



while is_race_on:
    if user_bet == red:
        rand_distance = random.randint(0, 50)
        turtle.forward(rand_distance)
    else:
        for turtle in bop_turtle:
            rand_distance = random.randint(0, 10)
            if turtle.pencolor().lower() == user_bet:
                rand_distance += 1
            turtle.forward(rand_distance)
           

            if turtle.xcor() > 218:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"Tu esi uzvareji! {winning_color} turtle is the winner!")
                    is_race_on = False
                else:
                    print(f"Tu esi zaudējis! {winning_color} turtle is the winner!")
                    is_race_on = False



    













screen.exitonclick()
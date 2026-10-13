import turtle
import time
import random

# Screen
win = turtle.Screen()
win.title("😂 Funny Snake Game")
win.bgcolor("lightblue")
win.setup(width=600, height=600)
win.tracer(0)

# Snake Head
head = turtle.Turtle()
head.shape("circle")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Funny Food
food = turtle.Turtle()
food.shape("turtle")
food.color("red")
food.penup()
food.goto(100, 100)

# Score
score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 16, "bold"))

segments = []

# Controls
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)
    if head.direction == "down":
        head.sety(y - 20)
    if head.direction == "left":
        head.setx(x - 20)
    if head.direction == "right":
        head.setx(x + 20)

win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

funny_food = ["🍕 Pizza", "🍔 Burger", "🍩 Donut", "🍟 Fries", "🌮 Taco"]

delay = 0.1

while True:
    win.update()

    # Border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        pen.clear()
        pen.write(
            f"🤣 Oops! You kissed the wall!\nFinal Score: {score}",
            align="center",
            font=("Arial", 14, "bold"),
        )
        break

    # Food collision
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        segment = turtle.Turtle()
        segment.shape("square")
        segment.color(random.choice(["blue", "yellow", "purple", "orange"]))
        segment.penup()
        segments.append(segment)

        score += 1

        pen.clear()
        pen.goto(0, 260)
        pen.write(
            f"Score: {score} | You ate {random.choice(funny_food)} 😂",
            align="center",
            font=("Arial", 16, "bold"),
        )

    # Move body
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Self collision
    for segment in segments:
        if segment.distance(head) < 20:
            pen.clear()
            pen.write(
                f"😂 You ate yourself!\nFinal Score: {score}",
                align="center",
                font=("Arial", 14, "bold"),
            )
            win.update()
            time.sleep(2)
            turtle.bye()

    time.sleep(delay)

win.mainloop()
# cube = [i+16 for i in range(1,11)]
# print(cube)


# odd  = [i for i in range(1,22) if i %2 != 0]
# print(odd)


# square = lambda x: x**2
# print(square(4))

# add = lambda x,y:x+y
# print(add(4,9))

# import turtle
# import time
# import random

# # Screen
# win = turtle.Screen()
# win.title("Snake Game")
# win.bgcolor("black")
# win.setup(width=600, height=600)
# win.tracer(0)

# # Snake head
# head = turtle.Turtle()
# head.shape("square")
# head.color("lime")
# head.penup()
# head.goto(0, 0)
# head.direction = "stop"

# # Food
# food = turtle.Turtle()
# food.shape("circle")
# food.color("red")
# food.penup()
# food.goto(100, 100)

# segments = []

# # Score
# score = 0
# delay = 0.1

# pen = turtle.Turtle()
# pen.speed(0)
# pen.color("white")
# pen.penup()
# pen.hideturtle()
# pen.goto(0, 260)
# pen.write("Score: 0", align="center", font=("Arial", 18, "bold"))

# # Movement functions
# def go_up():
#     if head.direction != "down":
#         head.direction = "up"

# def go_down():
#     if head.direction != "up":
#         head.direction = "down"

# def go_left():
#     if head.direction != "right":
#         head.direction = "left"

# def go_right():
#     if head.direction != "left":
#         head.direction = "right"

# def move():
#     x = head.xcor()
#     y = head.ycor()

#     if head.direction == "up":
#         head.sety(y + 20)
#     elif head.direction == "down":
#         head.sety(y - 20)
#     elif head.direction == "left":
#         head.setx(x - 20)
#     elif head.direction == "right":
#         head.setx(x + 20)

# # Keyboard
# win.listen()
# win.onkeypress(go_up, "Up")
# win.onkeypress(go_down, "Down")
# win.onkeypress(go_left, "Left")
# win.onkeypress(go_right, "Right")

# # Main loop
# while True:
#     win.update()

#     # Border collision
#     if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
#         time.sleep(1)
#         head.goto(0, 0)
#         head.direction = "stop"

#         for segment in segments:
#             segment.goto(1000, 1000)
#         segments.clear()

#         score = 0
#         delay = 0.1
#         pen.clear()
#         pen.write(f"Score: {score}", align="center",
#                   font=("Arial", 18, "bold"))

#     # Food collision
#     if head.distance(food) < 20:
#         x = random.randint(-280, 280)
#         y = random.randint(-280, 280)
#         food.goto(x, y)

#         new_segment = turtle.Turtle()
#         new_segment.shape("square")
#         new_segment.color("green")
#         new_segment.penup()
#         segments.append(new_segment)

#         score += 10
#         delay = max(0.05, delay - 0.002)

#         pen.clear()
#         pen.write(f"Score: {score}", align="center",
#                   font=("Arial", 18, "bold"))

#     # Move body
#     for i in range(len(segments)-1, 0, -1):
#         x = segments[i-1].xcor()
#         y = segments[i-1].ycor()
#         segments[i].goto(x, y)

#     if len(segments) > 0:
#         segments[0].goto(head.xcor(), head.ycor())

#     move()

#     # Self collision
#     for segment in segments:
#         if segment.distance(head) < 20:
#             time.sleep(1)
#             head.goto(0, 0)
#             head.direction = "stop"

#             for s in segments:
#                 s.goto(1000, 1000)
#             segments.clear()

#             score = 0
#             delay = 0.1

#             pen.clear()
#             pen.write(f"Score: {score}", align="center",
#                       font=("Arial", 18, "bold"))

#     time.sleep(delay)

# win.mainloop()


# mult = lambda x,y,z : x*y*z
# print(mult(4,6,3))

# biggest = lambda x,y : x if x>y else y
# print(biggest(6,9))


# num = lambda n: n if n%2 == on else 
# print(n)


# map 
 # =>  the map funtion is python applies a specific function true in an iteratable condition

# def age(n):
#     return "They can vote" if n>=18 else "they can't"

# num = [22,43,55,5,75,88]

# result = list(map(age, num))

# print(result)

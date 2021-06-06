import time, random
from init import *  

score = 0
segments = []

# Snake move
def move():
	if head.direction == "up":
		y = head.ycor()
		head.sety(y + 20)

	if head.direction == "down":
		y = head.ycor()
		head.sety(y - 20)

	if head.direction == "left":
		x = head.xcor()
		head.setx(x - 20)

	if head.direction == "right":
		x = head.xcor()
		head.setx(x + 20)

# keyboard handling
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

wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# check for collision with borders
def check_collision_borders():
	if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
		time.sleep(1)
		head.goto(0, 0)
		head.direction = "stop"				
	
		for i in segments:
			i.getturtle().reset()

		segments.clear()
		score = 0
# Main
while True:
	wn.update()
	
	check_collision_borders()

	# check for collision with food
	if head.distance(food) < 20:
		x = random.randint(-290, 290)
		y = random.randint(-290, 290)
		food.goto(x, y)

		new_segment = turtle.Turtle()
		new_segment.speed(0)
		new_segment.shape("square")
		new_segment.color('cyan')
		new_segment.penup()
		segments.append(new_segment)
		score = score + 10

	for index in range(len(segments)-1, -1,-1):
		x = segments[index-1].xcor()
		y = segments[index-1].ycor()
		segments[index].goto(x, y)

	if len(segments) > 0:
		x = head.xcor()
		y = head.ycor()
		segments[0].goto(x, y)

	wn.title("Snake game by UJJVAL | Score: " + str(score))
	move()
	time.sleep(delay)

wn.mainloop()

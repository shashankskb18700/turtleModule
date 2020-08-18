import math
import turtle
t=turtle.Turtle()
def circle(t,radius):
	circum=2*math.pi*radius
	n=100
	length=circum/n
	angle=360/n
	for i in range(n):
		t.fd(length)
		t.lt(angle)

	

circle(t,100)

import math
import turtle
t=turtle.Turtle()
def polygon(t,n,length):
	angle=360/n
	for i in range(n):
		t.fd(length)
		t.lt(angle)


polygon(t,n=7,length=70)

import os
import turtle

os.system("cls")

class Point(object):

	def __init__(self, x, y, color):
        	self.x = x
        	self.y = y
        	self.color = color

	def draw(self):
		turtle.penup()
		turtle.goto(self.x, self.y)
        	#turtle.pendown()
		turtle.color(self.color)
		turtle.setheading(0)
		self.draw_action()

	def draw_action(self):
        	turtle.dot(50,"red")
#==============================================================

class Box(Point):

	def __init__(self,x1,y1,width,height,color):
		self.x=x1
		self.y=y1
		self.width=width
		self.height=height
		self.color=color
		super().__init__(x1,y1,color)

	def draw_action(self):
		turtle.penup()
		turtle.goto(self.x, self.y)
		turtle.pendown()
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.right(90)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)

class BoxFilled(Box):
	def __init__(self,x1,y1, width, height, color, fillcolor):
		self.x=x1
		self.y=y1
		self.width=width
		self.height=height
		self.color=color
		self.fillcolor=fillcolor
		super().__init__(x1,y1, width, height, color)		

	def draw_action(self):
		turtle.penup()
		turtle.goto(self.x, self.y)
		turtle.fillcolor(self.fillcolor)
		turtle.begin_fill()
		turtle.pendown()
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.right(90)
		turtle.forward(self.width)
		turtle.right(90)
		turtle.forward(self.height)
		turtle.end_fill()	

class Circle(Point):
	def __init__(self,x1,y1,radius,color):
		self.x=x1
		self.y=y1
		self.radius=radius
		self.color=color
		super().__init__(x1,y1,color)

	def draw_action(self):
		turtle.penup()
		turtle.goto(self.x,self.y)
		turtle.pendown()
		turtle.circle(self.radius)
		
class CircleFilled(Circle):
	def __init__(self,x1,y1,radius,color,fillcolor):
		self.x=x1
		self.y=y1
		self.radius=radius
		self.color=color
		self.fillcolor=fillcolor
		super().__init__(x1,y1,radius,color)

	def draw_action(self):
		turtle.penup()
		turtle.fillcolor(self.fillcolor)
		turtle.begin_fill()
		turtle.goto(self.x,self.y)
		turtle.pendown()
		turtle.circle(self.radius)		
		turtle.end_fill()
#==============================================================
turtle.title("Lab Week 14 by Michael Bai")

print("###############################################################")
print("test Box subclass of accessing the attributes for the class")
b=Box(100,210,100,100,"red")
print("Box attritues access:")
print("x="+str(b.x)," y="+str(b.y)," width="+str(b.width), " height="+str(b.height)," color="+b.color)
b.draw() 	#!!!both super class and child class have draw_action! When calling function   of draw_action, it
		#call the child's draw_action. It sound like the draw is moved to the child class ---scope.
print("###############################################################")
b_fillcolor=BoxFilled(100,0,100,100,'blue','red')
print("BoxFilled attributes access:")
print("x="+str(b_fillcolor.x)," y="+str(b_fillcolor.y)," width="+str(b_fillcolor.width), " height="+str(b_fillcolor.height)," color="+b_fillcolor.color, " fillcolor="+b_fillcolor.fillcolor)
b_fillcolor.draw()
print("###############################################################")
c=Circle(-100,100,75,"green")
c.draw()
print("###############################################################")
c_fillcolor=CircleFilled(-100,-100,75,"red","blue")
c_fillcolor.draw()
print("###############################################################")
turtle.penup()
turtle.goto(-200,-200)
turtle.write("Wish everyone a very happy holiday season!       ",True,"center")

print("###############################################################")
c=input("pause for parent class")

 
 




 
 
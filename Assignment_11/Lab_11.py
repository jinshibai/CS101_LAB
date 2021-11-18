
import time
import os
os.system("cls")
import string

print ("#######################################################")
print ("Lab Week 13 - Classes: Clock tick")
print ("Michael Bai")
print ("#######################################################")
print ("\n\n")
######################################################################################
class Clock:
	def __init__(self,hour, minute, second,type=0):
		self.hour=hour
		self.minute=minute
		self.second=second
		self.hour2=hour
		self.type=type
		if type==0:
			self.type_value=""
		else:
			self.type_value="am"
	def tick(self):
		while True:
			m=0
			h=0
			init=0 #flag for no to print the first time.
			
			#no print the first one before processing.
			if init==0:
				print(self)
			init=1

			if self.second>=59:
				self.second=0
				m=1
			else:
				self.second +=1
			if self.minute>=59 and m==1:
				h=1
				self.minute=0
			else: 
				self.minute+=m 				
			if self.hour>=23 and m==1 and h==1:
				self.hour=0
			else:
				self.hour +=h
			#handle display type (12/24 hour format)
			if self.type==0:
				self.hour2=self.hour
			elif self.type==1 and self.hour<12:
				self.hour2=self.hour
				self.type_value="am"
			elif self.type==1 and self.hour>=12 and self.hour<13:
				self.hour2=self.hour
				self.type_value="pm"
			elif self.type==1 and self.hour>=13:
				self.hour2=self.hour-12
				self.type_value="pm"
			
			time.sleep(1)
	def __str__(self):
		return ("{:02d}:{:02d}:{:02d} ".format(self.hour2, self.minute,self.second)+self.type_value)  
######################################################################################
def check(x,min,max):
	msg=""

	try:
		i=int(x)
		if i>max or i<min:
			msg="\nPlease enter integer number between  "+str(min)+" and "+str(max)
	except:
		msg="\nwrong input.You must enter integer number between "+str(min)+" and "+str(max)


	if msg=="":
		return True
	else:
		print(msg)
		return False
######################################################################################

while True:
	x=input("What is the current hour ==> ")
	if check(x,0,24)==True:
		hour=int(x)
		break
while True:
	x=input("What is the current minute ==> ")
	if check(x,0,59)==True:
		minute=int(x)
		break
while True:
	x=input("What is the current second ==> ")
	if check(x,0,59)==True:
		second=int(x)
		break
while True:
	x=input("What is display type (0 for 12-hour format; 1 for 24-hour format ==> ")
	if check(x,0,1)==True:
		type=int(x)
		break
print("\n\n")
mytick=Clock(hour,minute,second,type)
mytick.tick()


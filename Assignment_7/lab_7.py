import re
import os
os.system('cls')

print ("#######################################################")
print ("Lab Week 8 - File handling, Try except")
print ("Michael Bai")
print ("#######################################################")
print ("\n\n")


def checkNumber(x):
	if x.isnumeric():
		return True

	y=list(x)
	if y[0]=="-" and x.replace("-","").isnumeric():
		return True
	return False

 		
i_minimum=""
 
while True:
	if i_minimum=="":
		print(" ================================= START =================================")
	while True:
		i_minimum=input("Enter the minimum mpg ==>")
 
		if checkNumber(i_minimum)==False:
			print("You must enter a number for the fuel economy")
			continue
		elif float(i_minimum)<0:
			print("Fuel economy given must be greater than 0")
			continue
		elif float(i_minimum)>100:
			print("Fuel economy must be less than 100")
			continue
		else:
			break

	print("\n")

	while True:
		s_input_file = input("Enter the name of the input vehicle file ==>")
		try:
			with open(s_input_file, "r") as f:
			    break
		except:
			print("Could not open file "+s_input_file)
			continue

	print("\n")

	while True:
		s_output_file=input("Enter the name of the file to output to ==> ")
		try:
			fw=open(s_output_file,"w")
			break
		except IOError as err:
			print("There is an IO Error to open  "+s_output_file+" in writing mode")
			continue

	print("\n")

	f = open(s_input_file, "r")
	fw=open(s_output_file,"w")
	firstLine=0
	for x in f:
		x_list=x.split("\t")
		if len(x_list)>1: #handle blannk line
			#print(x_list)
			#print(x_list[0],x_list[1])
			t1=x_list[0]+"\t"+x_list[1]
			t2=x_list[2] 
			t3=x_list[7]	

			if checkNumber(t3)==False and firstLine==1:
				print("Could not convert value "+t3+"  for vehicle "+ x_list[0]+" "+x_list[1]+" "+x_list[2])
			elif firstLine==1 and int(t3)>=int(i_minimum) : 
				t3="{:.3f}".format(int(t3))
				fw.write(t1.ljust(34)+t2.ljust(40)+t3.rjust(20)+"\n")
				print (t1.ljust(34)+t2.ljust(40)+t3.rjust(20)+"\n")	
		firstLine=1
	else:	
		print("\n\n\n")
		if input("try again y/Y? ==> ").lower()=="y":
			print(" \n\n================================ RESTART ================================")
		else:
			break
s=input("hold")
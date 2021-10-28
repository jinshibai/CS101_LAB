import os

from datetime import datetime

os.system("cls")
print('Name:Michael Bai')
print('LAB 8')
def add_test_assignment(x):

	y=input("Enter the "+x+" score 0-100 ==>")

	f=open(datafile,"a")

	f.writelines(x+","+y+"\n")

	f.close()
def remove_test_assignment(x):

	s_remove=""

	i_remove_total=0

	while True and x!=CLEAR_TEST and x!=CLEAR_ASSIGNMENT:

		s_remove=input("Enter the "+x+" to remove ==> ")
		try:

			i_remove=float(s_remove	)

		except:

			print("\nWrong input: You must enter number.")

			continue
		if i_remove<0:

			print("\nInput must be greater than zero.")

			continue
		break
	file_input=open("test.txt", "r")

	lines=file_input.readlines()  #content/object of all lines of the file!!!!!!

	file_input.close()
	output=open("test.txt", "w")
	for line in lines:

		line_item=line.split(",")

		if (x==CLEAR_TEST and line_item[0] ==TEST) or (x==CLEAR_ASSIGNMENT and line_item[0] ==ASSIGNMENT):

			i_remove_total=i_remove_total+1 

		elif line_item[0] == x and line_item[1].strip()	==s_remove.strip():	#!!!strip() 

			i_remove_total=i_remove_total+1

		else:

        		output.write(line)

	output.close()

	if i_remove_total==0:

		print("Could not find that score to remove")


def cal_mean(x):

	f=open("test.txt","r")

	i_sum=0.0

	i_count=0

	for i in f:

		s=i.split(",") 

		if s[0]==x.strip():

			i_count=i_count+1

			i_sum=i_sum+float(s[1])
	if int(i_count)!=0:

		i_sum=i_sum/i_count

	return i_sum
def cal_standard(x):

	i_mean=cal_mean(x)

	i_standard=0.0

	i_count=0

	i_min=9999.9

	i_max=0.0

	f=open("test.txt","r")

	for i in f:

		s=i.split(",") 
		if s[0].strip()==x.strip():

			i_standard=(i_standard+float(s[1])-i_mean)**2

			i_count=i_count+1

			if i_min>float(s[1]):

				i_min=float(s[1])

			if i_max<float(s[1]):

				i_max=float(s[1])

	if int(i_count)==0:

		s_result=("0","n/a","n/a","n/a","n/a")

	else:

		i_standard=(i_standard/i_count)**0.5

		s_result=(str(i_count),str(i_min),str(i_max),"{b:.2f}".format(b=i_mean),"{a:.2f}".format(a=i_standard))
	return s_result
def display_result():

	s_result_test=cal_standard(TEST)

	s_result_assignment=cal_standard(ASSIGNMENT)

	print("Type\t\t#\tmin\tmax\tavg\tstd")

	print("Tests\t\t"+s_result_test[0]+"\t"+s_result_test[1]+"\t"+s_result_test[2]+"\t"+s_result_test[3]+"\t"+s_result_test[4] )

	print("Programs\t"+s_result_assignment[0]+"\t"+s_result_assignment[1]+"\t"+s_result_assignment[2]+"\t"+s_result_assignment[3]+"\t"+s_result_assignment[4] )

	print("\n\n")

	print("The weighted sores is: "+str(cal_mean(TEST)*0.6+cal_mean(ASSIGNMENT)*0.4))
def display_menu():

	print("\n\n")

	print("		Grade Menu")

	print("1 - Add Test")

	print("2 - Remove Test")

	print("3 - Clear Tests")

	print("4 - Add Assignment")

	print("5 - Remove Assignment")

	print("6 - Clear Assignments")

	print("D - Display Scores")

	print("Q - Quit")

############		Main Program  		################

CLEAR_TEST="all_test"

TEST="test"

CLEAR_ASSIGNMENT="all_assignment"

ASSIGNMENT="assignment"

datafile="test.txt"

if os.path.exists(datafile)==True:

	os.remove(datafile)

#add first line to avoid error cuased by that  user to select remove/clear before adding anything

f=open(datafile,"a")

f.write("this file was created at "+str(datetime.now())+",#\n")

f.close()
while True:

	display_menu()

	choice=input("==>")
	if choice=="1":

		add_test_assignment(TEST)

	elif choice=="2":

		remove_test_assignment(TEST)

	elif choice=="3":

		remove_test_assignment(CLEAR_TEST)

	elif choice=="4":

		add_test_assignment(ASSIGNMENT)

	elif choice=="5":

		remove_test_assignment(ASSIGNMENT)

	elif choice=="6":

		remove_test_assignment(CLEAR_ASSIGNMENT)

	elif choice.upper()=="D":

		display_result()

	elif choice.upper()=="Q":

		quit()
if f.closed!=True:

	f.close()

if os.path.exists(datafile)==True:

	os.remove(datafile)


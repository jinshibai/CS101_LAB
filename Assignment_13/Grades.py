import math
import os
os.system("cls")
print ("#######################################################")
print ("Lab Week 15 ")
print ("Michael Bai")
print ("#######################################################")
print ("\n\n")
######################################################################################
#import Grades #!!! call self
def total(x):
	if not x:
		return 0.0
	else:
		s=0.0
		i_count=0
		for i in x:
			s=s+i
		return(s)
def average(x):
	if not x:
		return math.nan
	else:
		s=0.0
		i_count=0
		for i in x:
			s=s+i
			i_count=i_count+1
		return s/i_count
def median(x):
	try:
		x.sort()
		i_len=len(x)
		i_index=int(i_len/2)
		if i_len%2==0:
			return float((x[i_index-1]+x[i_index]))/2.0
		else:
			return x[i_index]
	except:
		raise ValueError
		return
# my test 
print(total([1, 10, 22]))
print(total([]))
print(average([2, 5, 9]))
print(average([]))
print(median([5, 2, 6, 1, 3]))
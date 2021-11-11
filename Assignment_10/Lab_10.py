import os
os.system("cls")
import string

print ("#######################################################")
print ("Lab Week 12 - Test 2")
print ("Michael Bai")
print ("#######################################################")
if __name__=="__main__" :
	while True:
		print("\n")
		filename=input("Enter the name of the file to open ==>")
		try:
			file=open(filename)
			break
		except:
			print("Could not open file "+filename)
	dict={}

	for i in file:
		list=i.strip().split(" ")

		for j in list:
			x=j.translate(str.maketrans('', '', string.punctuation)).lower()  # remove punctuation !!! must import string
			if len(x)>3:	#ignore word length of which is three or less than three characters.
				if x in dict:
					dict[x]=dict[x]+1
				else:
					dict[x]=1
	# sort the dictionary
	import operator
	dict2=sorted(dict.items(),key=operator.itemgetter(1),reverse=True) #sort in descending order !!!
	 
	print("\n")
	print("Most frequently used words")
	print("{0:<10}{1:>15}{2:>10}".format("#","Word","Freq."))
	print("======================================")

	i_index=1
	i_one=0
	i_unique=0
	for y in dict2:
		if i_index<=10:
			print("{0:<10}{1:<15}{2:>10}".format(str(i_index),y[0].strip(),str(y[1])))
			#print(str(i_index)+"\t"+y[0].strip()+"\t\t"+str(y[1]))	
			#print(y[0])
			i_index=i_index+1
		if y[1]==1:
			i_one=i_one+1

		i_unique=i_unique+1
	print("\n")
	print("There are "+str(i_one)+" words that occur only once")
	print("There are "+str(i_unique)+" words in the document")
	
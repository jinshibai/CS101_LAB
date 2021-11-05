import os
os.system("cls")
print ("#######################################################")
print ("Lab Week 10 - Dictionaries")
print ("Michael Bai")
print ("#######################################################")
print ("\n\n")


import csv
def isInteger(x):
	try:
		return int(x)
	except:
		return 0
################################################################################
def read_in_file(x):
	list=[]
	file=open(x, encoding="utf-8")  
	file_csv=csv.reader(file) 
	for line in file_csv:
		if line[1].strip() != "Reported_Date":
			list.append(line)

	if os.path.isfile(x)==True:
		file.close

	return list

def month_from_number(x):
	mlist=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	i=isInteger(x)

	if i >=1 and i<=12 and i!=0:
		return mlist[i-1]
	else:
		return "errir entry. Month must be 1 - 12"
	

def create_reported_date_dict(x):   
	keylist=read_in_file(x)
	key_count={}

	for key in keylist:
		if key[1] in key_count:
			key_count[key[1]]=key_count[key[1]]+1
		else:
			key_count[key[1]]=1
	return key_count

def create_reported_month_dict(x):
	keylist=read_in_file(x)
	key_count={}

	for key in keylist:
		temp=key[1].split("/")	#month of the date of record
		i=month_from_number(temp[0])
		if i in key_count:
			key_count[i]=key_count[i]+1
		else:
			key_count[i]=1
	return key_count	


def create_offense_dict(x):
	keylist=read_in_file(x)
	key_count={}

	for key in keylist:
		i=key[7].encode('utf-8') # to avoid encode error! 
		if i in key_count:
			key_count[i]=key_count[i]+1
		else:
			key_count[i]=1
	return key_count

	
 

def create_offense_by_zip(x):
	keylist=read_in_file(x)
	key_count={}
	list_offense=[]


	#create a list for OFFENSE: list_offense
	for y in keylist:
		if y[7] in list_offense :  
			itest=0
		else:
			list_offense.append(y[7])
	#..............................................................................
	for a in list_offense:
		itest=0
		key_sub={}
		for key in keylist:
			if a==key[7] :
				i=key[13]
				itest=itest+1
				if  i in key_sub:
					key_sub[i]=key_sub[i]+1
				else:
					key_sub[i]=1

		key_count[a]=key_sub
	return key_count
if __name__=="__main__":

	while True:
		try:
			file_name=input("Enter the name of the crime data file ==> ")
			file=open(file_name, encoding="utf-8")  
			file.close()
			break
		except:
			print("Could  not find the file specified. not exists not found.")
			continue
	month_dictionary=create_reported_month_dict(file_name)
	month_max_key=max(month_dictionary, key=month_dictionary.get) 
	month_max_value=max(month_dictionary.values())
	print("\n\n")
	print("The month with the  highest # of cirimes is "+month_max_key+" with "+str(month_max_value)+" offenses")

	offense_dictionary=create_offense_dict(file_name)
	offense_max_key=max(offense_dictionary, key=offense_dictionary.get)
	offense_max_value=max(offense_dictionary.values())
	print("The offense with the highest # of crimes is "+str(offense_max_key.decode('utf-8'))+" with "+str(offense_max_value)+" offenses")

	print("\n\n")
	while True:
		offense=input("Enter any offense ==>")
		result=create_offense_by_zip(file_name)

		if offense in  result:
			print("\n")
			print(offense +" offense by Zip code")
			sub_result=result[offense]
			print("Zip Code\t\t# of Offense")
			print("====================================")
			for s in sub_result:
				print(s+"\t\t\t"+str(sub_result[s]))
			
			break
		else:
			print("Not a valid offense found, please try again. ")
			continue

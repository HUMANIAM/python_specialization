import re
"""
this program sum all numbers in the file then print the result
"""

filename = input("Enter the file name : ")
try:
	filehandler = open(filename)
	pass
except Exception as e:
	print('sorry this file is not exist.')
	raise e

#you can read line by line extract numbers

sum = 0
for line in filehandler:
	numbers = re.findall('[0-9]+\.?[0-9]*', line)
	for number in numbers:
		sum = sum + int(number)
	pass
print(sum)

#the shortest way to do that is 
#print(sum([int(num) for num in re.findall('[0-9]+\.?[0-9]*', filehandler.read())]))

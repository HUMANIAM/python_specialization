"""
this very simple program is an introduction to python language. specifically, learning how to use functions and 
variable and casting it. so it is just an intro to new language.
"""

def Largest_smallest_val(numbers):
	smallest = largest = numbers[0]
	for x in range(1, len(numbers)):
		if numbers[x] > largest :
			largest = numbers[x]
		elif numbers[x] < smallest :
			smallest = numbers[x]
		else :
			continue
		
	return largest, smallest


def main():
	numbers = list()
	#get numbers from the user
	while True:
		num = input('Enter number : ')
		if num == 'done' :
			break
		try:
			numbers.append(int(num))	
		except :
			print('Invalid number')

	(largest, smallest) = Largest_smallest_val(numbers)
	print('Maximum is', largest)
	print('Minimum is', smallest)

	#we can say
	"""print('Maximum is', max(numbers))
	print('Minimum is', min(numbers))"""			
	
if __name__=="__main__":
	main()



	


    
    

    
    



    

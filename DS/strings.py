# read the file name
fname = input("Enter file name: ")
try:
	fh = open(fname)
	pass
except Exception as e:
	print('this file ',fname,' is not found')
	quit()
	raise e

senders = list()
parts   = list()

#count number of occurence of this pattern
count = 0
for line in fh:
	if line.startswith('From') and not line.startswith('From:'):
		count = count + 1
		parts = line.split()
		senders.append(parts[1])
		pass
	pass
	
#print out senders
for sender in senders:
	print(sender)
	pass
print('There were', count, 'lines in the file with From as the first word')



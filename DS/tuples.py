"""
 * program to read through the mbox-short.txt and figure out 
 *the distribution by hour of the day for each of the messages.
 """

# read the file and open it
filename = input("input the file name : ");
try:
	fhandler = open(filename);
	pass
except Exception as e:
	print("this file", filename, "is not found");
	raise e

#count how many times every sender sends
mssageperhrs = dict()

for line in fhandler:
	if line.startswith("From") and not line.startswith("From:"):
		words = line.split()
		time = words[5].split(':');
		mssageperhrs[time[0]] = mssageperhrs.get(time[0], 0) + 1;
		pass
	pass

#sort the message per hours by hours
sortedMessages = sorted([(k, v) for k,v in mssageperhrs.items()])

#print the sorted messages / hours
for hour, messages in sortedMessages:
	print(hour,messages)
	pass


"""
 this program reads through the mbox-short.txt and figure out who sent the greatest number of mail messages. 
 The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
"""
filename = input("input the file name");
try:
	fhandler = open(filename);
	pass
except Exception as e:
	print("this file", filename, "is not");
	raise e

#count how many times every sender sends
senders = dict()

for line in fhandler:
	if line.startswith("From") and not line.startswith("From:"):
		words = line.split()
		senders[words[1]] = senders.get(words[1], 0) + 1;
		pass
	pass

#find the sender who sends the maximum mails
maxmails = None
maxsender = None

for sender in senders:
	if (maxsender is None) or (senders[sender] > maxmails):
		maxsender = sender
		maxmails = senders[sender]
		pass

print(maxsender, maxmails)

#fastest way to get keys with the max values
print("*******\n")
maxmails =max(senders.values()) 
maxsender = list(filter(lambda x : senders[x] == maxmails, senders.keys()))
print(maxmails, "   ", maxsender)
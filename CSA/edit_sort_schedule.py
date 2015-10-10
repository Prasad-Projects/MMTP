temp1 = []
f = open("Sorted_Schedule.txt","r")
for line in f:
	a = line.split(' ')
	#print a
	if int(a[3]) > int(a[4]):
		#print a[3],a[4]
		temp = int(a[4]) + 24*60*60
		a[4] = str(temp)
		temp1.append(a)
		#print a[3],a[4]
	else:
		temp = int(a[4])
		a[4] = str(temp)
		temp1.append(a)
#print temp1
for x in temp1:
#	print x
	if x[0] == ' ':
		continue
	print x[0],x[1],x[2],x[3],x[4]
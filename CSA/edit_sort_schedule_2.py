temp1 = []
f = open("edited_sorted_schedule.txt","r")
for line in f:
	a = line.split(' ')
	#print a
	x = int(a[3]) + 24*60*60
	y = int(a[4]) + 24*60*60
	a[3] = str(x)
	a[4] = str(y)
	temp1.append(a)

#print temp1
for x in temp1:
	print x
	#if x[0] == ' ':
	#	continue
	#print x[0],x[1],x[2],x[3],x[4]
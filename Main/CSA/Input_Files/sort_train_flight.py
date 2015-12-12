from operator import itemgetter
L = []
f1 = open("Sorted_plane.txt","r")
for line1 in f1:
	line = line1.split(' ')
	L.append([line[0],line[1],line[2],int(line[3]),int(line[4])])

f2 = open("Sorted_Schedule.txt","r")
for line1 in f2:
	line = line1.split(' ')
	L.append([line[0],line[1],line[2],int(line[3]),int(line[4])])

temp = []
temp = sorted(L,key=itemgetter(3))
for item in temp:
	print item[0],item[1],item[2],item[3],item[4]

f1.close()
f2.close()
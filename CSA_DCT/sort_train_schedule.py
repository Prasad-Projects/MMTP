#Sort data according to departure time
from operator import itemgetter
L = []
#line = []
f = open("dct.txt","r")
for l1 in f:
	line = l1.split(" ")
	L.append([(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),(line[5][:-1])])
f.close()
temp = []
temp = sorted(L,key=itemgetter(3))
for item in temp:
	print item[0],item[1],item[2],item[3],item[4],item[5]

#Sort data according to departure time
from operator import itemgetter
L = []
line = []
for _ in xrange(44876):
	line = raw_input().split(" ")
	L.append([int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4])])
temp = []
temp = sorted(L,key=itemgetter(3))
for item in temp:
	print item[0],item[1],item[2],item[3],item[4]

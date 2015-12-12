#Sort data according to departure time
from operator import itemgetter
L = []
line = []
for _ in xrange(47377):
	line = raw_input().split(" ")
	L.append([(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4])])
temp = []
for item in L:
	if len(item[0])==5:
		print item[0],item[1],item[2],item[3],item[4],"train"


	elif len(item[0])>5:
		print item[0],item[1],item[2],item[3],item[4],"flight"

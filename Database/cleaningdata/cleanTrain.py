import sys
import MySQLdb
from time import strptime
from datetime import datetime

# Open database connection
Conn = MySQLdb.Connect(host="127.0.0.1",port=3306,user="root",passwd="12345",db="cleaningtrain")

cursor = Conn.cursor();

#Collecting station names and enumerating them for simplicity of computation 
sql = "select DISTINCT Station_Name from Train1"
cursor.execute(sql)
stnsEnumerate = {} #Enumerate the stations
results = cursor.fetchall()
ind=1


for row in results:
	if row[0] not in stnsEnumerate:
		stnsEnumerate[row[0]] = ind
		ind = ind + 1
		#print stnsEnumerate[row[0]],row[0]

#0    1    2 3     4     5       6    7   8 9      10   11          
#2779 TK   1 05:38 05:40 Tumkur 2779 YPR  1 06:43 06:45 Yesvantpur_Junction
f = open("trains1.txt","r")

	
	

TrainArray = []



for l in f:
	l1=l[:-1]
	line=l1.split(' ')
	#print line[4]
	sta=line[4].split(':')
	ste=line[9].split(':')
	#print ste[0],ste[1]
	start = (int(sta[1])*60)+((int(sta[0])%12)*3600)
	end = (int(ste[1])*60)+((int(ste[0])%12)*3600)
	if start>=end :
		end=(int(ste[1])*60)+(((int(ste[0])%12)+24)*3600)
		#print end
	TrainArray.append([int(line[0]),stnsEnumerate[line[5]],stnsEnumerate[line[11]],start,end])
		#for x,y,z in :
		#	print x
for it in TrainArray:
	print it[0],it[1],it[2],it[3],it[4]

Conn.close()


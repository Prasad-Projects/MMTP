import sys
import MySQLdb

# Open database connection
Conn = MySQLdb.Connect(host="127.0.0.1",port=3306,user="root",passwd="pass",db="loptest")

cursor = Conn.cursor();

#Collecting station names and enumerating them for simplicity of computation 
sql = "select DISTINCT src from NewWorld"
cursor.execute(sql)
stnsEnumerate = {} #Enumerate the stations
results = cursor.fetchall()
ind = 1

for row in results:
	if row[0] not in stnsEnumerate:
		stnsEnumerate[row[0]] = ind
		ind = ind + 1
#print stnsEnumerate

sql = "select DISTINCT dest from NewWorld"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
	if row[0] not in stnsEnumerate:
		stnsEnumerate[row[0]] = ind
		ind = ind + 1

#Forming an input file containing the following attributes per tuple
sql = "SELECT Train_num,src,dest,start,end,duration from NewWorld"

cursor.execute(sql)

TrainArray = []

results = cursor.fetchall()

for row in results:
	
	start = row[3].seconds#.split(':')
	end = row[4].seconds#.split(':')
	duration = row[5].seconds#.split(':')
	TrainArray.append([int(row[0]),stnsEnumerate[row[1]],stnsEnumerate[row[2]],row[3].seconds,row[4].seconds])
		#for x,y,z in :
		#	print x
for it in TrainArray:
	print it[0],it[1],it[2],it[3],it[4]

#Close db connection
Conn.close()


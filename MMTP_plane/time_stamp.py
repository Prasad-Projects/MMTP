import sys
import MySQLdb

# Open database connection
Conn = MySQLdb.Connect(host="127.0.0.1",port=3306,user="root",passwd="12345",db="lopoctober6")

cursor = Conn.cursor();

#Collecting station names and enumerating them for simplicity of computation 
sql = "select DISTINCT src from airline"
cursor.execute(sql)
stnsEnumerate = {} #Enumerate the stations
results = cursor.fetchall()
ind = 1

for row in results:
	if row[0] not in stnsEnumerate:
		stnsEnumerate[row[0]] = ind
		ind = ind + 1
#print stnsEnumerate
#airports=[]
#for row in results:
#	airports.append([row[0],stnsEnumerate[row[0]]])

sql = "select DISTINCT dest from airline"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
	if row[0] not in stnsEnumerate:
		stnsEnumerate[row[0]] = ind
		ind = ind + 1


#for row in results:
#	airports.append([row[0],stnsEnumerate[row[0]]])
#Forming an input file containing the following attributes per tuple
sql = "SELECT a_id,src,dest,start,end,duration from airline"

cursor.execute(sql)

PlaneArray = []

results = cursor.fetchall()

for row in results:
	
	start = row[3].seconds#.split(':')
	end = row[4].seconds#.split(':')
	duration = row[5].seconds#.split(':')
	PlaneArray.append([row[0].replace(" ","_"),stnsEnumerate[row[1]],stnsEnumerate[row[2]],row[3].seconds,row[4].seconds])
		#for x,y,z in :
		#	print x
for it in PlaneArray:
	print it[0],it[1],it[2],it[3],it[4]

#Close db connection
Conn.close()


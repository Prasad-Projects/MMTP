import sys
import MySQLdb
from time import strptime
from datetime import datetime

# Open database connection
Conn = MySQLdb.Connect(host="127.0.0.1",port=3306,user="root",passwd="12345",db="cleaningtrain")

cursor = Conn.cursor();



sql="select * from Train1";
cursor.execute(sql)
results = cursor.fetchall()

flag=0
row1=results[0]
row2=results[1]
for row in results:
	
	if flag==0:	
		row1=row
	
	elif flag>=1:
		if flag>1:	
			row1=row2		
		row2=row
		if not(row1[0]!=row2[0] or row1==row2):
			print row1[0],row1[1],row1[2],row1[3],row1[4],row1[5],row2[0],row2[1],row2[2],row2[3],row2[4],row2[5]		
	
	flag=flag+1

	
		

Conn.close()



#| Train_Num | stn_code | route | arr_time | dep_time    | Station_Name         |


from flask import Flask, render_template
import sys

from array import *

app = Flask(__name__)      
 
@app.route('/')
def home():
  return render_template('indes.php')

@app.route('/about')
def about():
  return render_template('about.html')
 
if __name__ == '__main__':
  app.run(debug=True)


MAX = 2**24 - 1 
NO_OF_STATIONS = 2000 #max number of stations
no_of_connections = 8281 #no of input connections
class Connections:
	def __init__(self,line):
			parameters = line.split(" ");

			self.train_no = int(parameters[0])
			self.dept_stn = int(parameters[1])
			self.arr_stn  = int(parameters[2])
			self.dep_time = int(parameters[3])
			self.arr_time = int(parameters[4])

def TimeTable(connections):
	#connections = []
	f = open("Sorted_Schedule.txt","r")
	for line in f:
		connections.append(Connections(line[:-1]))
		#print line[:-1]
	f.close()
	return;

#Station codes
Station_Code = {}




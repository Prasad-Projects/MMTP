#complete impplementation of t-CSA algorithm from paper
#IC array actually stores the connections, instead of indices into connections array.


import sys
import time
from array import *
from random import randint

#definition of infinity
MAX = 2**24 - 1

#class for connections stored in CA, DCTable
class Connections:
    def __init__(self,line):
        parameters = line.split(' ');

        self.train_no = parameters[0]
        self.dept_stn = int(parameters[1])
        self.arr_stn  = int(parameters[2])
        self.dept_time = int(parameters[3])
        self.arr_time = int(parameters[4])
        temp = parameters[5]
        self.label = temp[:-1]

#class for connections stored in OMTable
class OMTConnections:
    def __init__(self,line):
        parameters = line.split(' ');

        self.train_no = "om"
        self.dept_stn = int(parameters[0])
        self.arr_stn  = int(parameters[1])
        self.travel_time = int(parameters[2])

#method to convert an OMTConnection to Connection
def OMConvert(omt,dept_time):
    tempstr = omt.train_no + " " + `omt.dept_stn` + " " + `omt.arr_stn` + " " + `dept_time` + " " + `omt.travel_time + dept_time` + " " + "Other_Means" + "\n"
    return Connections(tempstr)


def CABuild(CA,CAFile):
    f = open(CAFile,"r")
    #f = open("connections.txt","r")
    for line in f:
        CA.append(Connections(line))

    f.close()
    return;


def DCTableBuild(DCTable,DCTableFile):
    f = open(DCTableFile,"r")
    for line in f:
        DCTable.append(Connections(line))

    f.close()
    return;


def OMTableBuild(OMTable,OMTableFile):
    f = open(OMTableFile,"r")
    #f = open("connections.txt","r")
    for line in f:
        OMTable.append(OMTConnections(line))

    f.close()
    return;

#method to build stations array (SA)
#SA stores mappings between station numbers and station names
#stations are identified only by station numbers in CA,DCTable and OMTable
def SABuild(SA,StationsFile):
    f = open(StationsFile,"r")
    for line in f:
        y = line[:-1].split(" ")
        str1 = ""
        for x in y[1:]:
            str1 += " " + x
        SA[int(y[0])] = str1
    f.close()
    return

#binary search through CA to find the right connection to start the CSA work
def ConnSearch(CA,deptime):
    first = 0
    last = len(CA)/3 - 1
    mid = 0
    while first <= last:
        if(CA[first].dept_time == deptime): break
        mid = (first+last)/2
        if deptime < CA[mid].dept_time:
            last = mid - 1
        else:
            first = mid + 1
    return mid


#search for direct connections; used in tCSA method
def searchDCT(Departure_Station, Arrival_Station, Departure_Time,DCTable,SA):
    for x in DCTable:
        if x.dept_stn == Departure_Station and x.arr_stn == Arrival_Station and x.dept_time >= Departure_Time:
            printConnection(x,SA)
            return x
    return None


#pretty print a connection
#x denotes connection; SA denotes station array
def printConnection(x,SA):
    while x.dept_time >= 86400:
        x.dept_time = x.dept_time % 86400
    while x.arr_time >= 86400:
        x.arr_time = x.arr_time % 86400

    hr1,min1 = x.dept_time/3600,(x.dept_time - (x.dept_time/3600)*3600)/60
    if hr1 < 10: hr1 = '0'+str(hr1)
    if min1 < 10: min1 = '0'+str(min1)

    hr2,min2 = x.arr_time/3600,(x.arr_time - (x.arr_time/3600)*3600)/60
    if hr2 < 10: hr2 = '0'+str(hr2)
    if min2 < 10: min2 = '0'+str(min2)
    print "{} {} to {} {}:{} {}:{} {}".format(x.train_no,SA[x.dept_stn],SA[x.arr_stn],hr1,min1,hr2,min2,x.label)
    return



#plain connection scan algorithm (CSA); algorithm-1 of the paper
def CSA(Departure_Station, Arrival_Station, Departure_Time,SA,CA):
    #Best Incoming connection as unsigned integer
    #one extra element required because stations are numbered from 1 onwards, not 0 where as array index bebings at 0
    IC = [None]*(len(SA)+1)
    #IC = array('I', [MAX for _ in range(no_of_connections)])
    #Arrival timestamp as unsigned integer
    Earliest_Arrival = array('I', [MAX for _ in range(len(SA)+1)])

    Earliest_Arrival[Departure_Station] = Departure_Time

    Min_Arrival = MAX
    for i in range(len(CA)):
        Ci = CA[i]

        if Ci.arr_time <= Earliest_Arrival[Ci.arr_stn] and Ci.dept_time >= Earliest_Arrival[Ci.dept_stn]:
            Earliest_Arrival[Ci.arr_stn] = Ci.arr_time
            IC[Ci.arr_stn] = Ci

            if Ci.arr_stn == Arrival_Station:
                Min_Arrival = min(Min_Arrival, Ci.arr_time)

        elif Ci.arr_time > Min_Arrival:
            break
        #elif (first_time + 2*length) <= i + 1:
        #    break

    return Itinerary(IC,Departure_Station, Arrival_Station,SA)




#improved CSA (tCSA); Algorithm-3 of the paper
def tCSA(Departure_Station, Arrival_Station, Departure_Time,DCTable,SA,TT,OMTable,CA):
    #x = searchDCT(2141,2143,randint(1,23)*60*60)

    omlength = len(OMTable)
    x = searchDCT(Departure_Station, Arrival_Station, Departure_Time,DCTable,SA)
    if x:
        return

    #print "CSA needs to run"
    #Best Incoming connection as unsigned integer
    #one extra element required because stations are numbered from 1 onwards, not 0 where as array index bebings at 0
    IC = [None]*(len(SA)+1)
    #print len(IC), len(SA)
    #IC = array('I', [MAX for _ in range(no_of_connections)])
    #Arrival timestamp as unsigned integer
    Earliest_Arrival = array('I', [MAX for _ in range(len(SA)+1)])

    Earliest_Arrival[Departure_Station] = Departure_Time
    i = ConnSearch(CA,Departure_Time)
    #printConnection(CA[i])	#OK, so far

    Min_Arrival = MAX
    first_time = i
    while i < len(CA):
        settled = False
        Ci = CA[i]

        #connection at an unvisited station can't be utilized
        if IC[Ci.dept_stn] == None and Ci.dept_stn != Departure_Station:
            #print j.dept_stn, Departure_Station
            i += 1
            continue

        #set transfer times
        if IC[Ci.dept_stn] == None:
            ttr = 0
        elif Ci.train_no == (IC[Ci.dept_stn]).train_no:
            ttr = 0
        else:
            ttr = TT[Ci.dept_stn]
        #print j.train_no,j.dept_stn,IC[j.dept_stn],ttr

        if Ci.arr_time <= Earliest_Arrival[Ci.arr_stn] and Ci.dept_time >= Earliest_Arrival[Ci.dept_stn]:
            #printConnection(j)
            settled = True
            Earliest_Arrival[Ci.arr_stn] = Ci.arr_time
            IC[Ci.arr_stn] = Ci
            #printConnection(IC[j.arr_stn])

            if Ci.arr_stn == Arrival_Station:
                Min_Arrival = min(Min_Arrival, Ci.arr_time)
                #print Min_Arrival
        elif Ci.arr_time > Min_Arrival:
            break
        #elif (first_time + 2*length) <= i + 1:
        #    break

        if settled:
            #print "check OMTable"
            for omi in range(omlength):
                tpossible = Ci.arr_time + OMTable[omi].travel_time
                if Ci.arr_stn == OMTable[omi].dept_stn and Earliest_Arrival[OMTable[omi].arr_stn] > tpossible:
                    Earliest_Arrival[OMTable[omi].arr_stn] = tpossible
                    ctemp = OMConvert(OMTable[omi],Ci.arr_time)
                    IC[OMTable[omi].arr_stn] = ctemp

        i += 1

    return Itinerary(IC,Departure_Station, Arrival_Station,SA)


#generates best route from IC array
#algorithm-2 of the paper
def Itinerary(IC,Departure_Station,Arrival_Station,SA):
    if IC[Arrival_Station] == None :
        print "NO TRAINS AVAILABLE STARTING THE SAME DAY"
        return None
    else:
        Route = []
        #Do Backtracking
        prev_connection = IC[Arrival_Station]
        no_of_iters = 70
        while prev_connection != None:
            no_of_iters-=1
            c = [prev_connection]
            Route[:0] = c
            #printConnection(temp)

            if prev_connection.dept_stn == Departure_Station: break
            prev_connection = IC[prev_connection.dept_stn]
            if no_of_iters == 0:
                print "Deadlock"
                print Departure_Station,Arrival_Station
                return None
            #print 'Out here'

        for x in Route:
            printConnection(x,SA)

    return Route

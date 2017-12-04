import sys
import csv
class Digraph:
    def __init__(self):
        self.temp = [] # temporarily queue

    def addModif(self,keyinput): #keyinput = [key+action,value]
        self.temp.insert(0,keyinput) #insert keyinput to a queue.
        if len(self.temp) == 3:
            act1 = self.temp.pop() # take away first value and store 2 others for next digraph
            act2 = self.temp[1]
            act3 = self.temp[0]
            time1 = abs(float(act1[1]) - float(act2[1]))
            time2 = abs(float(act3[1]) - float(act2[1]))
            time = float(time1/time2)
            print "time 1 = ", time1
            print "time 2 = ", time2
            print "time = time1/time2 = ", time
            key = act1[0] + act2[0] + act3[0]
            print "digraphID = ", key, "time of digraph = ", time
            return key, time
        else:
            return None, None

    def add(self,keyinput): #keyinput = [[key+action,value],[],[]]
            self.temp.insert(0,keyinput) #insert keyinput to a queue.
            if len(self.temp) == 2:
                act1 = self.temp.pop() # take away first value and store 2 others for next digraph
                act2 = self.temp[0]
                time = abs(float(act1[1]) - float(act2[1]))
                key = act1[0] + act2[0]
                print "digraphID = ", key, "time of digraph = ", time

                row = []
                row1 = []
                row2 = []
                row.append(key)
                row1.append(time)
                row2 = (row, row1)
                #print row
                #print row1
                print row2
                # out = open('out.csv', 'w')
                # columnTitleRow = "Digraph_ID, time\n"

                     # with open('out.csv', 'w') as csv_file:
                      # csv_writer = csv.writer(csv_file)
                    # for item in row2:
                      #csv_writer.writerows([row2])
                    # out.write(time)
                return key, time
            else:
                return None, None

sys.stdout = open('log.txt' , 'a')


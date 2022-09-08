import csv 

infile = open('steps.csv','r')

csvfile =  csv.reader(infile,delimiter=',')

next (csvfile)

if record[0] ==1:
    January +=record[1] 


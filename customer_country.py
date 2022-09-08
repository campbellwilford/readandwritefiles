import csv

def main():

    

    infile = open('customers.csv','r')

    csvfile = csv.reader(infile)

    outfile = open('customers_country.csv','w')

    csvfile =  csv.reader(infile,delimiter=',')

    for line in csvfile: 
        outfile.write((line[1]))
        outfile.write((line[2]))
        outfile.write((line[4]) +'\t\n')

   
    outfile.close()
    
main()


    



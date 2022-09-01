def main():

    import csv 

    infile = open('customers.csv','r')

    csvfile = csv.reader(infile)

    outfile = open('customers.csv','w')

    outfile.write('full name:',',','\n')
    outfile.write('country:',',','\n')
    outfile.write()

    outfile.close()
    
main()


    



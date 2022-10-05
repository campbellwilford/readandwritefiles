def main():

    import csv

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile, delimiter=',')

    outfile = open('avg_steps.csv','w')

    outfile.write('Month,Steps\n')

    monthNames = ['','January','February','March','Arpil','May','June','July','August','September','October','November']


    daycounter = 0
    step_total = 0
    month_cnt = 1

    next(csvfile)


    for rec in csvfile: 

        if int(rec[0])==month_cnt:  
            step_total += int(rec[1])
            daycounter += 1
        else:
            step_total = int(rec[1])
            daycounter = 1
            month_cnt +=1
 
    avg_steps =  round(step_total/daycounter,2)
    outfile.write(monthNames[month_cnt]+','+str(avg_steps)+'\n')           


    outfile.close()      
    
    

main()



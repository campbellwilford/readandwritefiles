def main():

    import csv

    infile = open('steps.csv','r')
    csvfile = csv.reader(infile, delimiter=',')

    outfile = open('avg_steps.csv','w')

    counter = 1 
    step_total = 0
    month_cnt = 0

    next(csvfile)


    for line in csvfile: 

        if line == month_cnt:   
            month_cnt += 1
            step_cnt = int(line[1])
            step_total = step_cnt + step_total
        else:
            monthly_avg = (step_total)/(month_cnt)
            outfile.write
            step_total=step_cnt + step_total
            avg_steps =  step_total/counter
    
    outfile.write() 
            

#I'll be honest I cannot figure this out I've been working on it for hours 
#I would have gone to your office hours but I had to drive to Dallas and I thought i would be able to figure it out in time that's my bad
#I'm accepting defeat
            
    
    

main()



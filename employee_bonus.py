import csv


infile = open('employeepay.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile)

for record in csvfile:
    ID = record[0]
    EmpFName = record[1]
    EmpLName = record[2]
    Salary = record[3]
    Bonus = record[4]
    TotalPay = str(int(record[3]) + (int(record[3]) * float(record[4])))
    
    print(format('ID:','20'))
    print(format('EmpFName:','20'))
    print(format('EmpLName','20'))
    print(format('Salary','20') + Salary)
    print(format('Bonus','20') + Bonus)
    print(format('TotalPay','20'))
    input()
    


    
    

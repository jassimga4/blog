import csv
from operator import add, delitem
import os


def display(section):
    with open(section + '.csv', 'r' ) as csv_file:
        reader = csv.reader(csv_file, delimiter = ',')
        i = 0
        for row in reader:
            print(i , row)
            i+=1

def deleterow(section, rowtodelete):

    #operation = input("edit(e) or delete(d): ")
    towrite= []
    with open(section + '.csv' , 'r') as file:
        data = csv.reader(file, delimiter = ',')
        for row in data:
            towrite.append(row)
    
    with open('output.csv' , 'w+' , newline = '') as file:
        myFile = csv.writer(file)
        i = 0
        for row in towrite:
            if i == rowtodelete:
                i+=1
            else:
                myFile.writerow(towrite[i])
                print(towrite[i])
                i+=1

    os.remove(section + '.csv')
    os.rename('output.csv', section + '.csv')

def adddata(section):
    while True:
        with open( section + '.csv','a',newline='') as file:
            myFile = csv.writer(file)
            name = input("Enter " + section + " name:")
            rating = input("Enter " +section + " rating:")
            if name and rating:
                print('input registered')
            else:
                print('Error empty input')
                break
            myFile.writerow([name , rating])

        display(section)
        check = input("Enter y to resume data input: ")
        if check.upper() == "Y":
            continue

        print("Data added")
        #exit and end program
        break
        



while True:
    section = input("Enter database to edit:")
    if section:
        display(section)
    else:
        break

    operation = input("Create new (n) or edit (e): ")
    if operation.upper() == "N":    
        adddata(section)
    elif operation.upper() == "E":
        rowtodelete = int(input("type number of row you wish to delete: "))
        deleterow(section , rowtodelete)

    
    exit = input("Press y to exit: ")
    if exit.upper() == "Y":
        print("Exiting")
        break
    else:
        continue








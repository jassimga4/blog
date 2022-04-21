import csv


section = input("Enter database to add to:")


while True:
    with open( section + '.csv','a',newline='') as file:
        myFile = csv.writer(file)
        name = input("Enter " + section + " name:")
        rating = input("Enter " +section + " rating:")

        myFile.writerow([name , rating])
    check = input("Do you want to add another entry? enter y + enter to resume data input:")
    if check.upper() == "Y":
        continue
    print("Program Ended")
    #exit and end program
    break

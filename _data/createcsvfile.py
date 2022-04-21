import csv

section_name = input("Enter desired filename:")

header = ['name', 'rating']
#change file name for sections
with open(section_name + '.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)




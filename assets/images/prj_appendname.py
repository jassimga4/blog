import os

for file_name in os.listdir():
    source = file_name
    destination = "prj_" + file_name
    os.rename(source, destination)

print ('filesrenamed')

print(os.listdir())
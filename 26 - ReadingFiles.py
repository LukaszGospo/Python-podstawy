file=open("26 - employees", "r")


for emp in file.readlines():
    print(emp)

file.close()
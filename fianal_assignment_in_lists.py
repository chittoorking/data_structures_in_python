fhandle = open('lists/file.txt')
for var in fhandle:
    data = var.split()
    print(data[2])
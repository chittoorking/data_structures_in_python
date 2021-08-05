fhandle = open("file.txt")
for var in fhandle:
    var = var.rstrip()
    line = var.upper()
    print(line)
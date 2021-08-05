fhandle = open("files/searching_file.txt")
#input = fhandle.read()
for line in fhandle:
    line=line.rstrip()
    if line.startswith('name'):
        print(line)
fhandle = open("files/searching_file.txt")
for line in fhandle :
    line = line.rstrip()
    if line.startswith('name'):
        continue
    print(line)
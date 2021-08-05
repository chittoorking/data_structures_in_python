fname= input("Please enter the file name you want to open")
try:
    fhandle = open("files/"+fname)
except:
    print("Bad file name ! can't open the file ")
    quit()
count = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('college'):
        print(line)
        count = count+1
print(count)
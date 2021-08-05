fname= input("Enter File ")
print(fname)
fhandle = open(fname)
for lines in fhandle:
    words = lines.split()
count = dict()
for word in words:
    count[word] = count.get(word,0)+1
largest = -1
theword = None
for k,v in count.items():
    print(k,v)
    if v > largest :
         largest = v
         theword = k
print("Done",theword,largest)
total = 0
count = 0
while True:
    inp =input('Enter the number')
    if inp =='done' : break
    inp = float(inp)
    total = total + inp
    count = count +1
average = total/count
print("total : ",total)
print("average",average)

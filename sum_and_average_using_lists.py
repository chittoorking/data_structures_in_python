numlist = list()
while True:
    inp = input("enter the number ")
    if inp =='done':break
    value= float(inp)
    numlist.append(value)
print('sum is ',sum(numlist))
print('Average is ',sum(numlist)/len(numlist))
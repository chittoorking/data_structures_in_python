c ={'a':10 ,'b':1 ,'c':22}
tmp =list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
#Reverse will not work in print statement 
print((sorted(tmp))) 
#Ascending order
tmp3 = sorted(tmp,reverse=True)
print(tmp3)
#descending order
tmp2 = list()
for k,v in sorted(tmp):
    tmp2.append((v,k))
print(tmp2)
#shortcut 
#Dynamically Creating and sorting 
print(sorted([(k,v) for v,k in c.items()]))
print(sorted([(k,v) for v,k in c.items()],reverse=True))
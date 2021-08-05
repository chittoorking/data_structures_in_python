fname = input ("Enter the file name ")
data = open(fname)
words = list()
for line in data:
     line = line.rstrip()
     words = line.split()
count=dict()
for word in words:
    count[word]=count.get(word,0)+1
res =sorted([(k,v) for v,k in count.items()],reverse=True) 
for a,b in res:
    print(b,a)

#Below is the second way of doing the same
   
"""fname = input('Enter File ')
if len(fname) < 1 fname = 'file.txt'>    hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5] :
    print(k,v)"""
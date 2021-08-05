#loops and dictionaries
#retrieving data using loops from dictioanries
data = {'hens':3,'sheep':10,'Lion':19}
for key in data:
    print(key,data[key])

#We can retrieve data without using loops also
#Here are the few ways
print(data)
print(list(data))
print(data.keys())
print(data.values())
print(data.items())
#See that data.items() returns a list having key value pair as each item in  thte list
for a,b in data.items():
    print(a,b)

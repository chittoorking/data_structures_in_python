slicing = [9,42,45,90,8,6]
print(slicing[3:5])
print(slicing[:4])
print(slicing[3:])
print(slicing[:])
print(slicing)
#building a list from scratch
stuff = list()
stuff.append('vamsi')
stuff.append(1)
print(stuff)
#using 'in' in searching
stuffing=[1,2,3,4,5,6,7,8,9,10]
print(9 in stuffing)
print(100 in stuffing)
print(120 not in stuffing)
#sorting of list items
names=['ramesh','raghu','amamla','jaga','vamsi']
print(names)
names.sort()
print(names)
#you cannot apply sorting if your list contains elements of varied types like below
mix =[1,'vamsi']

#Tuple can be put on the left hand side assignment statement
(x,y)=(1,'vamsi')
print(y)
(a,b)=(99,190)
print(a,b)
#The items() methos in dictionaries returns a list of (key,value) tuples
d={'vamsi':1,'pooja':2}
print( d.items())
# The comparison operators work with tuples and other sequences .If first item is equal ,python will go to the next element and so on until it finds elements that differ
print((1,2,3)<(3,4,5))

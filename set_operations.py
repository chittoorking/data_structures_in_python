#Union
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = set1.union(set2)
print(set3)
set4 = {7,8,9,6}
print(set3|set4)
#intersection
set5 = set1.intersection(set2)
print(set5)
print(set1&set2)
#subtraction
set6 = set1-set2
print(set6)
print(set2.difference(set1))
#symmetric difference
set8 = set1.symmetric_difference(set2)
print(set8)
print(set1^set2)
#A-B != B-A
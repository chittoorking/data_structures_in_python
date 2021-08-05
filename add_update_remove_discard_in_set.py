set_courses = {"Pyhton","DS","ML"}
print(set_courses)
set_courses.add("OOPS")
print(set_courses)
set_courses.update(['c1','c2'])
print(set_courses)
set_courses.discard("c2")
print(set_courses)
#we can discard  the element even if the element is not present in the set
set_courses.discard("c2")
#We cannot remove an element if an element is not present in the set 
#set_courses.remove("c2")
#pop() method will remove the last item.But the sets are unordered .So we will not know what item gets removed
# the return value of the pop method is the item removed
#sets are unordered hence pop function returns different elements in each programme execution
x=set_courses.pop()
print(x)
print(set_courses)
#We can delete the set in two ways
set_courses.clear()
print(set_courses)
del set_courses
#clear method deletes the elements of the set while delete method deletes the set from memory 
#print(set_courses)
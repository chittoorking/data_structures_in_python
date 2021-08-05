# len() function takes a list as a parameter and returns the number of elements in the list
list = [1,2,3,4,5,6,7,8,9,10]
print(len(list))
#list tells us the number of elements of any set ot sequence


#range function returns a list of numbers that range from 0 to 1 less than the parameter
#we can construct index loop using for and an integer iterator
print(range(len(list)))
students=['ravi','naveen','vamsi']
#first way to print elements of a list
for i in students:
    print("Hello",i)
#second way to print elements of a list
for i in range(len(students)):
    print("Hello",students[i])

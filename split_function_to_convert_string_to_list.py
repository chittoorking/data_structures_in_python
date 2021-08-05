str = "I am chittoor vamsi vara chandra reddy"
stuff = str.split()
print(stuff)
for words in stuff :
    print(words)

# when we don't specify a delimiter ,multiple spaces are treated as delimiter
sre2 ='This;is;a;single;string'
result1=sre2.split()
print(result1)
result2=sre2.split(';')
print(result2)
print(result2[1])
#example
line = 'From vamsi@gmail.com 07 bf'
words=line.split()
print(words)
gmail=words[1]
domain=gmail.split('@')
print(domain)
print("The domain is ",domain[1])




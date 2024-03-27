#SETS {}
'''

set1={'dhanraj','ajay','ajit','shri'}
set2={'apple','banana','cherry'}

print (type(set1))

len_set1=len(set1)
print (len_set1)

len_set2=len(set2)
print (len_set2)

set1={'praveen','ajay','san'}
set2={'joy','fun','run','san'}
print (type(set1))
len_set1=len(set1)
len_set2=len(set2)
print ("length of {0} is {1}\nLength of {2} is {3}".format(set1,len_set1,set2,len_set2))
print (dir(set1))
usrin=input("Enter the element to be added\n")
set1.add(usrin)
print (set1)

print (set1.intersection(set2))

'''



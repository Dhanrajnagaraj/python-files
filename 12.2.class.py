a1=[10,20,30,40]
b1=[50,60,70,80,90]
if (len(a1) == len(b1)):
    print ("Length of Both lists {0} and {1} are same".format(a1,b1))
    c1=a1+b1
    print ("Combined list {0} and {1} is {2}".format(a1,b1,c1))
    post=int(input("Enter the position number\n"))
    print ("Position {0} exists element is {1}".format(post,a1[post]))
    print ("Position {0} exists element is {1}".format(post,b1[post]))
    cout=a1[post]+b1[post]
    print ("Sum is {0}".format(cout))

elif (len(a1) != len(b1)):
    print ("Length of {0} and {1} are not same".format(a1,b1))
    a1_len=len(a1)
    b1_len=len(b1)
    c1_len=a1_len-b1_len
    print ("Length of {0} is {1}\nLength of {2} is {3}\nDifference of length is {4}".format(a1,a1_len,b1,b1_len,c1_len))

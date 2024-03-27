a="kiran"
for i in a:
    if (i == "a"):
        break
    else:
        print (i)

        

a=input("Enter the input\n")
bre=input("Enter the charecter to upto break\n")
for i in a:
    if (i == "bre"):
        break
    else:
        print (i)



a=input("Enter the input\n")
bre_ch=input("Enter the character for breaking\n")
bre_pos=int(input("Enter the position number\n"))
for i in range(0,len(a),1):
    if ( i == bre_pos ):
        break
    else:
        print (a[i])


        
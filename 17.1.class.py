a=input("Enter the input\n")
bre_ch=input("Enter the character for breaking\n")
bre_pos=int(input("Enter the position number\n"))
for i in range(0,len(a),1):
    if (i == bre_pos):
        if (a[i] == bre_ch):
            break
        else:
            print (a[i])

    else:
        print (a[i])



alist=['kiran','ajit','10','20','shri','om']
for i in alist:
    if (i == 20):
        break
    else:
        print(i)
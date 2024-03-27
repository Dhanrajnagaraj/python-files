# ## Dictionary
#
# dict_ex={'a':'10','b':'20','c':'30'}
# print (type(dict_ex))
# print (len(dict_ex))
# print (dict_ex['a'])
# print (dict_ex['b'])
# print (dict_ex.keys())
# print (dict_ex.values())
# print (dict_ex.items())
# keylist = dict_ex.keys()
# print (keylist)
# keylist = list(dict_ex.keys())
# print (keylist)
# valuelist = list(dict_ex.values())
# print (valuelist)
# print ("type is {0}\nValue are {1}\nKey is {2}\nValue is {3}".format(type(dict_ex),dict_ex,keylist,valuelist))
#

# dict_ex={'a':'10','b':'20','c':'30'}
# dict_ex['d']='40'
# print(dict_ex)

# dict_ex={'a':'10','b':'20','c':'30'}
# keyinput=input("enter the key\n")
# valueinput=input("enter the value\n")
# dict_ex[keyinput]=valueinput
# print(dict_ex)
# print ("post adding {0} and {1} into dictionary, new details of dictionary is {2}".format(keyinput,valueinput,dict_ex))

# dict_example={'a':'10','b':'20','c':'30'}
# print (dict_example)
# keyinpu=input("Enter the keyname\n")
# print (keyinpu in dict_example)
# print ("Current value of {0} is {1}".format(keyinpu,dict_example[keyinpu]))
# newvlaue=input("Enter the new value for key {0}".format(keyinpu))
# dict_example[keyinpu]=newvlaue
# print (dict_example)
# print ("After updating the key {0}, New value of key is {1}".format(keyinpu,dict_example[keyinpu]))

# dict_example={'a':'10','b':'20','c':'30'}
# dum_list={'e':'apple','f':'banana','g':'orange'}
#
# dict_example.update(dum_list)
# print(dict_example)

# dict_example.pop('a')       #removing key a from dictionary
# print(dict_example)

# rmkey=input("enter the key to be removed\n")
# dict_example.pop(rmkey)
# print(dict_example)


dict_demo={}
list1=['a','b','c']
list2=['apple','banana','cherry']
dict_demo[list1[0]]=list2[0]
print(dict_demo)



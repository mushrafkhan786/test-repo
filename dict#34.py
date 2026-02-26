##dic = {
##    580: "Mushraf",
##    340:"Ishwar",
##    400:"krishna",
##    440:"yash"
##}
##
##print(dic[440])
##
##info ={'name':"sakil",'age':'22','job':'welder'}
##print(info)
##print(info['name']) #if i take a word not in dic gives error
##print(info.get('name'))#if i take a word not in dic gives none
##print(info.keys())
##print(info.values())
##
###we can iterate by for loop
##for key in info.keys():
##    print(info[key])
##
##print(info.items())
##for key,value in info.items():
##    print(f"The value coresponding to key {key} is {value}")
##


#dict methods
ep1 = {200:50,201:80,202:65,203:89}
ep2={209:56,210:90,211:66}

##ep1.update(ep2)
##ep1.clear()
##ep1.pop(202) #remove 202
ep1.popitem()  #it removes the last item
##del ep1
#delete the dict and if give give key then del particular key

print(ep1)





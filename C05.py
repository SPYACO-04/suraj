# Dectionaries and sets
'''it is unordered
it is mutable
it is indexed
canot have duplicate keys'''


'''
marks={
    "harry":100,
    "subham":56,
    "suraj":23
}
print(marks,type(marks)) #{'harry': 100, 'subham': 56, 'suraj': 23}  <class 'dict'>
print(marks["subham"])   #56
print(marks.items())     #dict_items([('harry', 100), ('subham', 56), ('suraj', 23)])
print(marks.keys())      #dict_keys(['harry', 'subham', 'suraj'])
print(marks.values())    #dict_values([100, 56, 23])
marks.update({"harry":99,"renuka":100})
print(marks)
print(marks.get("harry3"))  #None
print(marks.pop("suraj"))   #23

'''


#SETS

s={1,2,3,4,5,5,5,5,5}

e=set() #empty set
print(s)

print(s,type(s))  # {1, 2, 3, 4, 5} <class 'set'>
s.add(325)
print(s,type(s)) # {1, 2, 3, 4, 5, 325} <class 'set'>
s.remove(3)
s.add(32)
print(s,type(s))


s1={1,23,45,52,53}
s2={42,42,64,34,65,23}
print(s1.union(s2))
print(s1.intersection(s2))
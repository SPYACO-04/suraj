#list is represent by square brackects []
# we can store different data types in a list
# friends=["apple","Orange" ,5, 345.06, False, "ammit", "Rohan"]
# print(friends[0])
# friends[0]="Grapes"#Unlike strings lists are mutable
# print(friends[0])
# print(friends[1:4])

# l1=[1,34,432,43,64,32,24]
# l1.sort()
# l1.reverse()
# l1.insert(3,23423) # it inserts 23423 at index3
# print(l1.pop(3))
# value=l1.pop(3)
# print(value)
# print(l1)
# print(l1.remove(64))
# print(l1)

#tuple is represented as paranthesis : ()
# we can't chane the value of tuple once is created
t1=(1,34,432,43,64,32,24,False, "Suraj","Ram")
print(t1)
print(t1.count(34)) # it return the index of first occurence of 34
i=t1.index("Suraj")
print(i)
print(len(t1))
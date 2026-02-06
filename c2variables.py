'''a=1
b=3
c=4
d="suraj"
print(a+b)
d=False
e=None'''

# Arithmatic Operators.(+,-,*,/,%,//,**)
a=3
b=4
c=a+b
print(c)

#assignment Operators.(=,+=,-=,*=,/=,%=,//=,**=)
a = 4-2
print(a)
b = 6
#b +=3 #increment the value of b by 3 and then assign it to b
b -=3 #Decrement the value of b by 3 and then assign it to b.
print(b)

#Comarision Operators.(!,<,>,<=,>=,==)
d = 5!=3
print(d)

#Logical Operators.(and,or,not)
e = True or False
print(e)
print(not False) #not operator convert True to False and False to true.

# Types

a = "32.5"
b = float(a) # a but the type should be flaot
t = type(b) #class <int>
print(t)

#Input Functon :

a = int(input("Enter your number 1 :"))
b = int(input("Enter your number 2 :"))
print("the number a is :",a)
print("the number b is :",b)
print("the sum is:",(a+b))
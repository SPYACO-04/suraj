#A2Q1.
'''
per = float(input("Enter percentage: "))

if per >= 90:
    print("Grade: A+")
elif per >= 80:
    print("Grade: A")
elif per >= 70:
    print("Grade: B")
elif per >= 60:
    print("Grade: C")
elif per >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")
'''
# A2Q2.

'''
num = input("Enter a 5-digit number: ")

print("Digits at odd positions:")
for i in range(len(num)):
    if i % 2 == 0:   # index starts from 0
        print(num[i])
'''
# A2Q3
'''
num = input("Enter a number: ")

if num == num[::-1]:
    print("Palindrome number")
else:
    print("Not a palindrome number")
'''
# A2Q4
'''
num = int(input("Enter a number: "))
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")
'''
# A2Q5
'''
num = int(input("Enter a 3-digit number: "))
print("Prime factors are:")

for i in range(2, num + 1):
    if num % i == 0:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            print(i)
'''
# A2Q6
'''
s = input("Enter a string: ")
vowels = 0
consonants = 0

for ch in s.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Reversed string:", s[::-1])
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
'''

# A3Q1
'''
n = int(input("Enter value of N: "))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Twin prime numbers are:")
for i in range(2, n - 1):
    if is_prime(i) and is_prime(i + 2):
        print(i, i + 2)
'''

# A3Q2
'''
num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial is:", fact)
'''

# A3Q3
'''
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
'''

# A3Q4
s = input("Enter a string: ")

# Palindrome check
'''
if s == s[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")

# Symmetrical check
mid = len(s) // 2
if len(s) % 2 == 0:
    if s[:mid] == s[mid:]:
        print("Symmetrical string")
    else:
        print("Not symmetrical")
else:
    if s[:mid] == s[mid + 1:]:
        print("Symmetrical string")
    else:
        print("Not symmetrical")
'''

# A3Q5
'''
sentence = input("Enter a sentence: ")
words = sentence.split()

print("Even length words are:")
for word in words:
    if len(word) % 2 == 0:
        print(word)
'''

# A3Q6
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)

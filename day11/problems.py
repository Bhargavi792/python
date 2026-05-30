a = 15
b = 10
print("Addition", a + b)

#problem2
a = 50
b = 18
print("Subtraction", a - b)

#problem3
a = 12
b = 5
print("Multiplication", a * b)

#problem4
a = 25
b = 4
print("Division",a / b)

#problem5
a = 25
b = 6
print("Modulus", a % b)

#problem6
a = 5
b = 3
print("Exponentiation", a ** b)

#problem 7
a = 17
b = 3
print("Floor Division", a // b)

#problem 8
a = 12
b = 10
c = 2
d = 8 
print("Arithmetic expression", a * b // c + d)

#problem 9
num = 27

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#problem 10
a = 10
b = 20

a, b = b, a

print(a, b)

#problem 11
length = 15
width = 8

area = length * width
print(area)

#problem 12
p = 10000
r = 5
t = 2

si = (p * r * t) / 100
print(si)

#problem 13
a = 45
b = 32

print(a > b)

#problem 14
x = 100
y = 100

print(x == y)

#problem 15
age1 = 20
age2 = 18

print(age1 >= age2)

#problem 16
age = 19
citizen = True

print(age >= 18 and citizen)

#problem 17
username = "admin"
password = "1234"

print(username == "admin" and password == "1234")

#problem 18
num = 15

print(num >= 10 and num <= 20)

#problem 19
x = 10

x += 5

print(x)

#problem 20
x = 8

x *= 4

print(x)

#problem 21
a = 12
b = 45
c = 30

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)


#problem 22
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


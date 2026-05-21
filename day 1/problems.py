# problem1

name = "bhargavi"
college_name = "scient institute of technology"
branch = "AIML"
print("Name", name)
print("College name", college_name)
print("Branch", branch)

# problem2

student_name = "bhargavi"
roll_number = 60
maths = 75
science = 80
social = 90
total_marks = maths + science + social
avg_marks = total_marks / 3
print("Student name", student_name)
print("Roll number", roll_number)
print("Total marks", total_marks)
print("Average marks", avg_marks)

# PROBLEM3
A = 20
B = 20
addition = A + B
subtraction = A - B
multiplication = A * B      
division = A / B
print("Addition",addition)  
print("Subtraction",subtraction)
print("Multiplication",multiplication)
print("Division",division)


# problem3(other way)
A = 20
B = 20    
print("Addition", A + B)
print("Subtraction", A - B)        
print("Multiplication", A * B)
print("Division", A / B)

# problem4

a = 5
b = 8
a, b = b, a
print("a=", a)
print("b=", b)

# problem4(other way)

a = 5
b = 8
temp = a
a = b
b = temp
print("a=", a)   
print("b=", b)

# problem5

length = 5
breadth = 4
area = length * breadth
print("Area of rectangle", area)

# problem6

radius = 7
pi = 3.14
area = pi * radius * radius
print("Area of circle", area)

# problem7

side = 5
area = side * side
print("Area of square", area)

#problem8
print("Hello, World!")

#problem9
x = 2
square = x * x
print("Square:", square)

#problem10
y = 10 
cube = y * y * y
print("Cube:", cube)

#problem11
price = 499
print(type(price))

#problem12

x = 5
y = "John"
print(x)
print(y)

#problem13
x = 4
x = "Sally"
print(x)

#problem14(casting)
x = str(3) #x will be '3'
y = int(3) #y will be 3 
z = float(3) #z will be 3.0

#problem15
X = 5
Y = "John"
print(type(X))      
print(type(Y))

#problem16(CAMAL CASE)
myVariableName = "bhargavi"
#pascal case 
MyVariableName = "bhargavi"
#snake case
my_variable_name = "bhargavi"

#problem17(many to one variable)
a, b , c ="orange", "banana", "cherry"
print(a)
print(b)
print(c)

#problem18(one to many variable)
x = y = z = "mango"
print(x)
print(y)
print(z)

#unpacking a collection
#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#problem19(global variable)
x = "great"
def myfunc():
  print("Python is " +x)
myfunc()

#problem20(local variable)
x = "awesome"
def myfunc():               
  x = "fantastic"
  print("Python is " + x)   

myfunc()
print("Python is " + x) 

#problem21
def myfunc():
  global x
  x = "fantastic"   
myfunc()
print("Python is " + x)

#problem22
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) 

#problem23
a = "vattapu"
b = "bhargavi"
print(a + " " + b)

#problem24
is_student = True
print(is_student)
print(type(is_student))

#problem25
a = 10
#integer to float
b = float(a)
print(b)
print(type(b))
#float to integer
x=15.5
z=int(x)
print(z)
print(type(z))
#integer to string
a=10
b=str(a)
print(b)
print(type(b))

#problem26(si = (P*R*T)/100)
principal = 1000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

#problem27(temp celcius to fahrenheit)(F=9/5*C+32)
celsius = 30
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#problem28(temp fahrenheit to celcius)(C=5/9*(F-32))
fahrenheit = 86 
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)   

#problem29
python_marks = 85
java_marks = 90
dbms_marks = 80
highest_marks = max(python_marks, java_marks, dbms_marks)
print("Highest marks:", highest_marks)

#problem30(total bill)
item_name = "pen"
quantity = 10
price_per_item = 2.5
total_bill = quantity * price_per_item
print("Total bill:", total_bill)

#problem31
weight = 70
height = 1.75   
bmi = weight / (height ** 2)
print("BMI:", bmi)

#problem32
current_year = 2026
birth_year = 2005
age = current_year - birth_year
print("Age:", age)




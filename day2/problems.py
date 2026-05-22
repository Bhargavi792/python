 #problem 1
a = "bhargavi"
b = 21
c = 5.4 
d = "wheather you are student"
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(c))

#problem 2
a = 5
b = 3
print("addition",a+b)
print('subtraction',a-b)
print("multiplication",a*b)
print("division",a/b)

#problem 3
price = 99.99
b = int(price)
c = str(price)
print(b)
print(c)

#problem 4
is_python_fun = True
a = is_python_fun
print(a)
print(type(a))

#problem 5
full_name = "v.bhargavi"
print("first character",full_name[0])
print("last character",full_name[-1])
print("length of the string",len(full_name))

#problem 6
a = "50"
b = 20
c = int(a)
print("addition",b+c)

#problem 7
a = ["integer","float","string","boolean"]
print(list(a))

# problem 8
x = 3 + 4j
print("value of x:",(x))
print(type(x))
print("real part",x.real)
print("imaginary part",x.imag)

# problem 9
a = ["maths","social","science","gk","english"]
print("first subject",a[0])
print("last subject",a[-1])
print("total no.of subjects",len(a))

# problem 10
a = (10,29,35,24)
print("tuple:",a)
# trying to change number
a [1] = 30

# problem 11
a = {"name": "bhargavi" ,"roll number": 60,"branch" : "aiml"}
print(a["name"])
print(a["roll number"])
print(a["branch"])

# problem 12
numbers = {1, 2, 3, 2, 1, 4}
print(set(numbers))

# problem 13
celsius = 45
b = (9/5 * celsius + 32)
print("celsius",celsius)
print("fahrenheit",b)
print(type(celsius))
print(type(b))

# problem 14
name = "bhargavi"
roll_no = 60
height = 5.4
is_student = True 
subjects = ["maths","social","science"]
marks = {"maths":60,"social":38,"science":76}
print("------student profile-----")

print("Name:",name)
print("Roll NO:",roll_no)
print("height:",height)
print("is_student:",is_student)
print("subjects:",subjects)
print("marks:",marks)

# problem 15
a = 10
b = "20"

# Conversions
a = str(a)
b = int(b)

# Convert a back to integer for addition
result = int(a) + b

print("a after conversion:", a)
print("Datatype of a:", type(a))

print("b after conversion:", b)
print("Datatype of b:", type(b))

print("Addition:", result)

# problem 16
student = {
    "name": "Bhargavi",
    "marks": [80, 90, 85]
}

# Printing student name
print("Student Name:", student["name"])

# Calculating average marks
average = sum(student["marks"]) / len(student["marks"])

print("Average Marks:", average)

# problem 17
a = True
b = 10
c = a + b
print(c)
print(type(c))



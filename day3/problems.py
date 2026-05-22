#problem1
a = "25"
b = "4"
print("remainder",25%4)

#problem2
a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#problem3
a = 10
b = 25
c = 15

if a <= b and a <= c:
    print("smallest:", a)
elif b <= a and b <= c:
    print("smallest:", b)
else:
    print("smallest:", c)

#problem4
num = 123

reverse = int(str(num)[::-1])

print("Reversed Number =", reverse)        
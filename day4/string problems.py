#problem1
name = "bhargavi"
print("NAme:",name)

#problem2
a = "banana"
print("first character:",a[0])

#problem3
a = "raheem"
print("last character:",a[-1])

#problem4
a = "RAHEEM"
print("lower case:",a.lower())

#problem5
a = "raheem"
print("upper case:",a.upper())

#problem6
a = "ice"
b = "apple"
print("concatenate:",a+b)

#problem7
for x in "banana":
 print(x)

#problem8
text = "bhargavi"
char = "r"
if char in text:
    print("character exits")
else:
    print("character doesnot exit")

#problem9
text = "education"

count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        count += 1

print(count)

#problem10
text = "python"

print(text[::-1])

#problem11
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

  #problem12
  text = "PyThOn"

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

#problem13
text = "python programming"

print(text.replace(" ", "_"))

#problem14
text = "Python is easy"

words = text.split()

print(len(words))

#problems15
text = "programming"

result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)



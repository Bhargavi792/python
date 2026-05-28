#problem1
text = "python"
print(text.upper())

#problem2
text = "PYTHON"
print(text.lower())

#problem3
text = "python programming"
print(text.capitalize())

#problem4
text = "banana"
print(text.count("a"))

#problem5
text = "hello world"
print(text.find("world"))

#problem6
text = "I Love Python"
print(text.replace("Python","Java"))

#problem7
text = "   hello   "
print(text.strip())

#problem8
text = "python"
print(text.startswith("py"))

#problem9
website = "google.com"
print(website.endswith(".com"))

#problem10
text = "Python is easy"

print(text.split())

#problem11
words = ["Python", "is", "fun"]

print(" ".join(words))

#problem12
text = "python developer"
words = text.split()
print(len(words))

#problem13
text = "pillow"
print(text[::-1])

#problem14
text = "madam"

if text == text[::-1]:
 print("palindrome")
else:
     print("it is not palindrome")

#problem15
text = "programming"

vowels = "aeiou"

result = ""

for ch in text:
    if ch not in vowels:
        result += ch
print(result)

#problem16
text = "python is powerful"

print(text.title())

#problem17
text = "12345"

print(text.isdigit())

#problem18
text = "Python"

print(text.isalpha())

#problem19
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

#problem20


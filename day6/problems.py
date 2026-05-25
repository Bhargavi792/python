#problem1
text = "python"
print("upper case:",text.upper())

#problem2
text = "PYTHON"

print(text.lower())

#problem2
text = "PYTHON"

print(text.lower())

#problem3
text = "   hello world   "

print(text.strip())

#problem4
text = "I like Java"

print(text.replace("Java", "Python"))

#problem5
text = "banana"

print(text.count("a"))

#problem6
text = "python programming"

print(text.capitalize())

#problem7
text = "hello world"

print(text.upper())

#problem8
text = "python is easy"

print(text.replace(" ", "-"))

#problem9
text = "Python"

print(text[::-1])

#problem10
text = "Python"

print(text.startswith("Py"))

#problem11
text = "programming"

print(text.endswith("ing"))

#problem12
text = "Python is powerful"

print(text.split())

#problem13
words = ["Python", "is", "easy"]

print(" ".join(words))

#problem14
text = "programming"

vowels = "aeiou"

result = ""

for ch in text:
    if ch not in vowels:
        result += ch

print(result)

#problem15
text = "PyThOn"

print(text.swapcase())

#problem16
text = "Artificial Intelligence"

print(len(text))

#problem17
text = "python programming language"

print(text.title())

#problem18
text = "Machine learning is fun"

words = text.split()

print(len(words))

#problem19
text = "programming"

result = ""

for ch in text:
    if ch not in result:
        result += ch

print(result)


#problem20
text = "Python is an amazing language"

words = text.split()

longest = max(words, key=len)

print(longest)

#problem21
text = "HELLO"

result = ""

for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].lower()
    else:
        result += text[i].upper()

print(result)

#problem22
text = "Madam"

text = text.lower()

print(text == text[::-1])

#problem23
text = "Python is easy"

print(text.replace(" ", "\n"))

#problems24
text = "Artificial Intelligence"

vowels = "aeiouAEIOU"

result = ""

for ch in text:
    if ch in vowels:
        result += ch

print(result)


#problem25

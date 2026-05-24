#problem1

text = "bhargavi"
print(text[:3])

#problem2
text = "bhargavi"
print(text[-4:])

#problem3
text = "bhargavi"
print(text[::-1])

#problem4
text = "bhargavi"
print(text[::2])

#problem5
text = "wonderfull"
print(text[1:-1])

#problem6
text = "language"
print(text[2:7])

#problem7
text = "bhargavi"
print(text[-3:1])

#problem8
text = "bhargavi"
print(text[:5][::-1])

#problem9
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#problem10
email = "bhargavi@gmail.com"
start = email.index("@") + 1
end = email.index(".")

print(email[start:end])

#problem11
text = "python programmer"
print(text[::-2])

#problem12
text = "database"
 
mid = len(text) // 2
print(text[:mid])
print(text[mid:])

#problem13
text = "artifical"
print(text[2:-2])

#problem14
text = "bharu"
new_text = text[-1] + text[1:-1] + text[0]

print(new_text)

#problem15
text = "python is easy"
words = text.split()
print(words[::-1])

#problem16
text 
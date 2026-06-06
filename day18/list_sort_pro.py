#problem 1
numbers = [50, 20, 70, 10]

numbers.sort()

print(numbers)

#problem 2
numbers = [50, 20, 70, 10]

numbers.sort(reverse=True)

print(numbers)

#problem 3
names = ["Ravi", "Anu", "Bhargavi", "Kiran"]

names.sort()

print(names)

#problem 4
words = ["Python", "AI", "Programming", "Code"]

words.sort(key=len)

print(words)

#problem 5
data = [(1, 5), (2, 3), (4, 1)]

data.sort(key=lambda x: x[1])

print(data)
#problem 1
fruits = ["Apple", "Banana", "Mango"]

for item in fruits:
    print(item)

#problem 2
fruits = ["Apple", "Banana", "Mango"]

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1

#problem 3
fruits = ["Apple", "Banana", "Mango"]

for i in range(len(fruits)):
    print(i, fruits[i])

#problem 4
numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

print(total)

#problem 5
numbers = [10, 50, 20, 70, 30]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

#problem 6
numbers = [10, 50, 20, 70, 30]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

#problem 7
numbers = [2, 3, 4, 5, 6, 7, 8, 11]

for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

#problem 8
numbers = [1, 2, 3, 4, 5, 6]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)


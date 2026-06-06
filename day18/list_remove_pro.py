#problem 1
fruits = ["Apple", "Banana", "Mango"]

fruits.remove("Banana")

print(fruits)

#problem 2
fruits = ["Apple", "Banana", "Mango"]

fruits.pop()

print(fruits)

#problem 3
fruits = ["Apple", "Banana", "Mango"]

del fruits[0]

print(fruits)

#problem 4
fruits = ["Apple", "Banana", "Mango"]

fruits.clear()

print(fruits)

#problem 5
numbers = [10, 20, 10, 30, 10]

while 10 in numbers:
    numbers.remove(10)

print(numbers)

#problem 6
numbers = [1, 2, 2, 3, 4, 4, 5]

numbers = list(set(numbers))

print(numbers)

#problem 7
numbers = [1, 2, 3, 4, 5, 6]

numbers = [num for num in numbers if num % 2 != 0]

print(numbers)


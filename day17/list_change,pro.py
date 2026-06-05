#problem1
mylist = [ "apple" , "banana" , "mango" , "lichi" , "papaya" , "grapes"]

mylist[0] = "orange"
print(mylist)

#problem2
mylist = [ "apple" , "banana" , "mango" , "lichi" , "papaya" , "grapes"]

mylist[-1] = "orange"
print(mylist)

#problem 3
mylist = [ "apple" , "banana" , "mango" , "lichi" , "papaya" , "grapes"]

mylist[2] = "python"
print(mylist)

#problem 4
mylist = [ "apple" , "banana" , "mango" , "lichi" , "papaya" , "grapes"]

mylist[1:4] = ("orange" , "python" , "dsa")
print(mylist)

#problem 5
mylist = [ "apple" , "banana" , "mango" , "lichi" , "papaya" , "grapes"]

for i in range (len(mylist)):
    mylist[i] = mylist[i].upper() 
    
    print(mylist)


#problem 6
mylist = [ "apple" , "banana" , "mango" , "lichi" , "papaya" , "grapes"]

for i in range (len(mylist)):
    mylist[i] = mylist[i].upper() 
    
print(mylist)

#problem 7
numbers = [ 2 , 4 , 8, 9]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = 0
        
print(numbers)     



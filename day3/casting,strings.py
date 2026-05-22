'''
->Random Number
Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

ex:import random
print(random.randrange(1, 10)

->(Strings)
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

->Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

->Strings are Arrays
Like many other popular programming languages, strings in Python are arrays of unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
Example:
a = "Hello, World!"
print(a[1])

->Looping Through a String
Since strings are arrays, we can loop through the characters in a string, with a for loop.
ex:for x in "banana":
  print(x)

 ->Check String
To check if a certain phrase or character is present in a string, we can use the keyword in. 
Example
Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

->Use it in an if statement:

Example
Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

->Check if NOT
To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

->Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.

->Slice From the Start
By leaving out the start index, the range will start at the first character:

Example
Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

->Slice To the End
By leaving out the end index, the range will go to the end:

->Upper Case
ExampleGet your own Python Server
The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())

->Lower Case

->Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

Example
The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

->Replace String
The replace() method replaces a string with another string:

->Split String
The split() method returns a list where the text between the specified separator becomes the list items.

->String Concatenation
To concatenate, or combine, two strings you can use the + operator.
To add a space between them, add a " ":

->String Format
we cannot combine strings and numbers like this
But we can combine strings and numbers by using f-strings or the format() method!

->F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
 
->Placeholders and Modifiers
A placeholder can contain variables, operations, functions, and modifiers to format the value.

Example
Add a placeholder for the price variable:

price = 59
txt = f"The price is {price} dollars"
print(txt)

->Escape Characters
Other escape characters used in Python:

Code	Result	Try it
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value


'''
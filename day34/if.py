'''
#if statements
#supports logical conditions

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b

How If Statements Work
The if statement evaluates a condition (an expression that results in True or False). If the condition is true, the code block inside the if statement is executed. If the condition is false, the code block is skipped.

#Indentation
-> we will use white spac ebefore if statement to run the block
->if not it occurs error

#Multiple Statements in If Block
You can have multiple statements inside an if block. All statements must be indented at the same level.


#variables in conditions
Boolean variables can be used directly in if statements without comparison operators.

Using a boolean variable:

is_logged_in = True
if is_logged_in:
  print("Welcome back!")

 Python can evaluate many types of values as True or False in an if statement.

Zero (0), empty strings (""), None, and empty collections are treated as False. Everything else is treated as True.
 

'''
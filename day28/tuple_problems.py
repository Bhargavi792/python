# Problematic: Creates an integer
not_a_tuple = (5)  # type: int

# Correct: Creates a tuple
a_tuple = (5,)  # type: tuple

#
# Modifying Immutability (TypeError)Problem: Attempting to add, remove, or change elements raises a TypeError.Cause: Tuples are strictly immutable sequences.Solution: Convert the tuple to a mutable list, make modifications, and convert it back
data = (10, 20, 30)

# Workaround to "append" or modify
temp_list = list(data)
temp_list.append(40)
data = tuple(temp_list)  # Output: (10, 20, 30, 40)

#problem











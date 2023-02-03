# Here is a function that returns "hello world" in ASCII numbers:

def hello_ascii():
    hello_world = "Hola mundo"
    ascii_numbers = [str(ord(char)) for char in hello_world]
# The ASCII code is a numerical representation of each character in the alphabet and can be found using the ord() function in Python.
# In this code, the list comprehension [str(ord(char)) for char in hello_world] iterates over each character in the string "hello_world". 

# For each character, the ord() function is used to find its ASCII code value, and this value is then converted to a string using str().
# The result is a list of ASCII code values, 
# represented as strings, for each character in the "hello_world" string. 
# The list comprehension stores this result in the variable ascii_numbers.
 
    return " ".join(ascii_numbers)
# Create a variable for join all the strings in the function

print(hello_ascii())
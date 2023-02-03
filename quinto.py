# A function that accepts a matrix of 10 integers (between 0 and 9), 
# that returns a string of those numbers in the form of a phone number.

# The function uses the format method of strings to insert the numbers 
# from the matrix into the desired format. The syntax *numbers unpacks 
# the array and passes each element as a separate argument to the format
#  function. The result will be a string with the format (123) 456-7890.

def createPhoneNumber(numbers):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*numbers)

print(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

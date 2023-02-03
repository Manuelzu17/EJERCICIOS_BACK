# Here is a function in Python that can extract all numbers from a list
#  of numbers from 1 to 100 that are equal when passed as an argument to
#  the function, and return its result:

def extract_equal_numbers(numbers_list, target_number):
    result = []
    for number in numbers_list:
        if number == target_number:
            result.append(number)

# The append method in Python is used to add an element to the end of a list. 

    return result

numbers = list(range(1, 101))
target = 8
equal_numbers = extract_equal_numbers(numbers, target)

print("Result",equal_numbers)
print("List", numbers)


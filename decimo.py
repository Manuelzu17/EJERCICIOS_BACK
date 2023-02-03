import random

def change_data_types(dic):
    for key in dic:
        value = dic[key]
        # Generate a random number between 0 and 2
        choice = random.randint(0, 2)
        if choice == 0:
            # Change value to string
            dic[key] = str(value)
        elif choice == 1:
            # Change value to float
            dic[key] = float(value)
        else:
            # Change value to int
            dic[key] = int(value)
    return dic

# Example dictionary
example_dict = {'a': 1, 'b': 2.0, 'c': '3'}

# Change data types
result = change_data_types(example_dict)

# Print the result
print(result)

import random

random_list = []

for i in range(100):
    random_list.append(random.randint(0, 100))
# This uses the randint function from the random library to generate 
# random numbers and add them to the random_list. 
# The random_list will be printed at the end.

print(random_list)

# You can use a regular expression in Python to remove duplicated
# characters from five different strings and convert them into a
# single string without duplicates. Here's an example code that
# takes five strings and combines them into one string without
# duplicate characters using a regular expression:

import re
# import regex This module provides regular expression 
# matching operations similar to those found in Perl. 

# Definition of a function with a tupla, is an union of strings
def remove_duplicates(*input_strings):

# Create a variable for join all the strings in the function
    combined = ''.join(input_strings)
    return ''.join(sorted(set(re.findall(r'(?i)(\w|\d)', combined)), key=lambda x: combined.index(x)))
# it uses the re.findall function to extract all the alphanumeric
#  characters (letters and numbers) from the combined string.

# The (?i) flag in the regular expression (regex) pattern r'(?i)
# (\w|\d)' makes the search case-insensitive. The (\w|\d)
# part of the regex pattern matches either a word character
# (alphanumeric character or underscore) or a digit.
 
# After that, the set function is used to remove any duplicates 
# from the extracted characters, as sets only contain unique 
# elements. 
# 
# Finally, the sorted function sorts the list of unique characters 
# using the key parameter set to a lambda function lambda x: 
# combined.index(x). This lambda function takes an element 
# from the list of unique characters and returns its index 
# in the combined string, which is then used as the sorting key. 
# This way, the resulting list is sorted in the order that the 
# characters appear in the original combined string.
#  

print(remove_duplicates("F,7N3Sj2]E%F34q;xn6JZ6P5%4iF", "+TSha.zQd?.;{3=*mTn![p-&FE4k&f", "p@%.$K:iq3MmuNmWNmxd[,S+AN#SB.", "G:+/3A@fQeu]wJt}!+@mu3PCtRSnv2", "m&gz8Gt)/7Dd7vixHc?+H,F8YfC$Wd"))

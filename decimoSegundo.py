def most_common_sequence(char_list):
    from collections import Counter

    # Create a dictionary of sequences and their frequencies
    sequences = Counter([''.join(char_list[i:i+n]) for n in range(1, len(char_list) + 1) for i in range(len(char_list) - n + 1)])

    # Return the sequence with the highest frequency
    return sequences.most_common(1)[0][0]

# Example usage
characters = ['a', 'b', 'c', 'a', 'b', 'd', 'b']
print(most_common_sequence(characters)) # Output: 'ab'

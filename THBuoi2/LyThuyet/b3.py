def count_chars(inp_str):
    inp_str = inp_str.strip().lower()
    char_count = {}
    for char in inp_str:
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

test_string = ' Happiness '
assert count_chars(inp_str=test_string) == {'h': 1, 'a': 1, 'p': 2, 'i': 1, 'n': 1, 'e': 1, 's': 2}

string = ' smiles '
print(count_chars(string))

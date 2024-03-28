def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    word_count = {}
    words = text.split()
    for word in words:
        word = word.lower()  
        if word.isalpha():  
            word_count[word] = word_count.get(word, 0) + 1

    return word_count

file_path = 'P1_data.txt'
assert count_words(file_path)['success'] == 3

print(count_words(file_path)['man'])

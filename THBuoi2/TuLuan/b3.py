def count_letters(word):
    word = word.lower()
    letter_count = {}
    for letter in word:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1])
    return sorted_letter_count
def count_word_frequecy(word):
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print( frequency)

words = ['apple',"orange","banana","apple","orange","apple"]
count_word_frequecy(words)

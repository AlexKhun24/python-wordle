

def dictionary_initialization(word):
    key_and_count = dict.fromkeys(list(word), 0)
    keys = key_and_count.keys()

    # letters_and_count dictionary set up to keep track of letter "key" and word count "value"
    for key in keys:
        counter = 0
        for letter in word:
            if key == letter:
                counter += 1
        key_and_count[key] = counter

    return key_and_count
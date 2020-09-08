import re

def find_repeated_word(text):
    """
    Function finds the first repeated word in a string and returns this word.
    """
    if not isinstance(text, str):
        raise TypeError

    word_list = []
    text_list = re.findall(r'[A-Za-z]+', text.lower())

    for word in text_list:
        if word in word_list:
            return word
        word_list.append(word)

    return('There is no repeated word!')

def count_words(text):
    """
    Function takes a string and returns a count of each of the words in the provided string.
    """
    if not isinstance(text, str):
        raise TypeError

    word_list = {}
    text_list = re.findall(r'[A-Za-z]+', text.lower())

    for word in text_list:
        if word in word_list:
            word_list[word] += 1
        else:
            word_list[word] = 1

    return word_list

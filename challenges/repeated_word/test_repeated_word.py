from repeated_word import find_repeated_word, count_words
import pytest

def test_text():
    text = "Once upon a time, there was a brave princess who..."
    assert find_repeated_word(text) == "a"

def test_big_text():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert find_repeated_word(text) == "it"

def test_no_repeated():
    text = "Once upon time, there was a brave princess who..."
    assert find_repeated_word(text) == "There is no repeated word!"

def test_text_with_punctuation():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    assert find_repeated_word(text) == "summer"

def test_input():
    text = 1
    with pytest.raises(TypeError):
        result = find_repeated_word(text) 

def test_count_words():
    text = "Once upon a time, there was a brave princess who..."
    assert count_words(text)['once'] == 1
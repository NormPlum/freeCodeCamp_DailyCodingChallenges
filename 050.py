# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-29

def get_longest_word(sentence):
    longest = ""
    words = sentence.split()
    for word in words:
        if len(word.strip(".")) > len(longest):
            longest = word.strip(".")
    return longest

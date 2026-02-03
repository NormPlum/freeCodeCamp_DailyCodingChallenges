# https://www.freecodecamp.org/learn/daily-coding-challenge/2025-09-14

def get_words(paragraph):
    result = []

    word_count = {}
    words = paragraph.split()
    for word in words:
        word = word.strip(",.!").lower()
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    sorted_words = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    sorted_keys = sorted_words.keys()
    for i, word in enumerate(sorted_keys):
        if i < 3:
            result.append(word)

    return result

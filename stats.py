def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    characters = {}
    for character in text:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters
    
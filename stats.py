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

def sort_on(dictionary):
    return dictionary["num"]

def sort_dict(dictionary, path, count):
    list_of_characters = []
    for key, value in dictionary.items():
        list_of_characters.append({"char": key, "num": value})
    list_of_characters.sort(reverse=True, key=sort_on)
    
    print(f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------""")

    for character in list_of_characters:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")

    print("============= END ===============")
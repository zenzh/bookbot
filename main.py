from stats import count_words, count_chars

def main():
    text = get_book_text("./books/frankenstein.txt")
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    print(count_chars(text))

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents.lower()

main()

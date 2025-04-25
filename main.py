from stats import count_words, count_chars, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    character_count = count_chars(text)
    word_count = count_words(text)

    sort_dict(character_count, path, word_count)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents = f.read()
    return contents.lower()

main()

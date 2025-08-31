import sys
from stats import word_count, get_book_text, letter_count, sort_letters

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    words =  0
    text = get_book_text(f"{book_path}")
    words = word_count(text)
    letters = letter_count(text)
    sorted_letters = sort_letters(letters, words)
    print(text)
    print(f"{words} words found in the document")
    print(letters)
    print(sorted_letters)
main()
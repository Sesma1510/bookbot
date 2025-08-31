def get_book_text(book_path):
    with open(f"{book_path}") as f:
        return f.read()

def word_count(text):
    return len(text.split())

def letter_count(text):
    dict = {}
    for letter in text.lower():
        if letter.isalpha():
            dict[letter] = dict.get(letter, 0) + 1
    return dict

def sort_letters(dict, word_count):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    lines = []
    lines.append("============ BOOKBOT ============")
    lines.append(f"Analyzing book found at books/frankenstein.txt...")
    lines.append("----------- Word Count ----------")
    lines.append(f"Found {word_count} total words")
    lines.append("--------- Character Count -------")
    for letter, count in sorted_dict:
        lines.append(f"{letter}: {count}")
    lines.append("============= END ===============")

    return "\n".join(lines)
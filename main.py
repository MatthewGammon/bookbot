def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    char_count = count_characters(text)

    print_report(book_path, num_words, char_count)
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_characters(text):
    chars = {}
    for c in text:
        if c.isalnum():  # Only count alphanumeric characters
            lowered = c.lower()
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def print_report(book_path, num_words, char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

main()
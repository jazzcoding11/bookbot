def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    char_count = {}
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            if lower_char in char_count:
                char_count[lower_char] += 1
            else:
                char_count[lower_char] = 1
    
    report_list = []
    for char, count in char_count.items():
        report_dict = {'char': char, 'count': count}
        report_list.append(report_dict)
    def count_value(dict_item):
        return dict_item['count']
    report_list.sort(reverse = True, key = count_value)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for item in report_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("\n--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def get_count_words(text):
        words = text.split()
        return len(words)
    
    def get_chars_dict(text):
        chars = {}

        for char in text:
            lower_char = char.lower()
            if lower_char in chars:
                chars[lower_char] += 1
            else:
                chars[lower_char] = 1

        return chars
    
    def convert_chars_dict_to_list(chars):
        chars_list = []

        for c in chars:
            chars_list.append({"char": c, "num": chars[c]})

        return chars_list
    
    def sort_chars_list(list):
        return sorted(list, reverse=True, key=lambda dict: dict["num"])
    
    def get_book_report():
        chars_dict = get_chars_dict(file_contents)
        chars_list = convert_chars_dict_to_list(chars_dict)
        sorted_chars_list = sort_chars_list(chars_list)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{get_count_words(file_contents)} words found in the document")
        print("\n")
        for char in sorted_chars_list:
            if char['char'].isalpha():
                print(f"The '{char['char']}' character was found {char['num']} times")
        print("--- End report ---")
    
    get_book_report()

main()
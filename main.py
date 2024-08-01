def main():
    path_to_file = 'books/frankenstein.txt'
    try:
        with open(path_to_file, 'r') as f:
            words = f.read()
            print("--- Begin report of books/frankenstein.txt ---")
            print(f"{count_words(words)} words found in the document \n")
            character_counts = count_characters(words)
            sorted_characters = convert_and_sort_characters(character_counts)
            for entry in sorted_characters:
                print(f"The '{entry['character']}' character was found {entry['count']} times")
    except FileNotFoundError:
        print(f"The file at {path_to_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def count_words(text):
    words = text.split()
    return len(words)



def count_characters(text):
    text = text.lower()  # Convert the text to lowercase
    character_counts = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            if char in character_counts:
                character_counts[char] += 1
            else:
                character_counts[char] = 1
    return character_counts

def convert_and_sort_characters(character_counts):
    # Convert dictionary to list of dictionaries
    char_list = [{'character': char, 'count': count} for char, count in character_counts.items()]
    # Sort the list by the count in descending order
    char_list.sort(key=lambda x: x['count'], reverse=True)
    return char_list



if __name__ == '__main__':
    main()

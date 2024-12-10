from pathlib import Path

def get_text(path_to_file: Path):
    with open(path_to_file) as fp:
        text = fp.read()
    return text

def count_words(text: str)->int:
    # prompt is to find 77986 "words"
    items = text.split()
    # omitted as this was overthinking the intended solution
    # words = []
    # for item in items: 
    #     if item.isalpha():
    #         words.append(item)
    return len(items)

def count_characters(text: str)->dict:
    character_counts = {}
    for character in text:
        character = character.lower()
        character_counts[character] = character_counts.get(character, 0) +1
    return character_counts

def print_report(text: str, path_to_file: Path)->None:
    word_count = count_words(text)
    character_count = count_characters(text)
    key, value = 0, 1
    sorted_character_counts = sorted(character_count.items(), key = lambda item: item[value])
    sorted_character_counts = sorted_character_counts[-1::-1]
    print(f"--- Begin report of {str(path_to_file)} ---")
    print(f"{word_count} words found in the document\n")
    for item in sorted_character_counts:
        if item[key].isalpha():
            print(f"The '{item[key]}' character was found {item[value]} times")
    print("--- End report ---")

def main()->None:
    path_to_file = Path("books","frankenstein.txt")
    text = get_text(path_to_file)
    print_report(text, path_to_file)
    
if __name__=="__main__":
    main()

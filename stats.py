def count_words(text: str)->int:
    # prompt is to find 77986 "words"
    items = text.split()
    return len(items)

def count_characters(text: str)->dict:
    character_counts = {}
    for character in text:
        character = character.lower()
        character_counts[character] = character_counts.get(character, 0) +1
    return character_counts
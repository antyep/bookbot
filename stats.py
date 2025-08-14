def get_num_words(text):
    words = text.split()
    return len(words)

def character_counter(text):
    counter = dict()
    for letter in text:
        letter_to_lower = letter.lower()
        if letter_to_lower in counter:
            counter[letter_to_lower] += 1
        else:
            counter[letter_to_lower] = 1
    return counter


def sort_characters(counter):
    sorted_characters = []
    for character, count in counter.items():
        convert_to_alpha = character.isalpha()
        if (convert_to_alpha):
            sorted_characters.append({
                "char": character,
                "num": count
            })

    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
        
def sort_on(char_dict):
    return char_dict["num"]

            


from dictionary import Dictionary

def dictionary_mode():
    dictionary = Dictionary("words.txt")
    while True:
        chosen_language = input("Would you like to translate from German to English (press GE) or from English to German (press EG)?")
        if chosen_language == 'GE':
            word_to_translate = input("which word do you want to translate?")
            translate_result = (dictionary.german_to_english(word_to_translate))
            if translate_result is not None:
                print(translate_result)
            else:
                print("The word you want to translate is not in the dictionary.")
        if chosen_language == 'EG':
            word_to_translate = input("which word do you want to translate?")
            translate_result = (dictionary.english_to_german(word_to_translate))
            if translate_result is not None:
                print(translate_result)
            else:
                print("The word you want to translate is not in the dictionary.")
        next_choice = input("Do you want to translate another word (Y / N)?").lower()
        if next_choice == 'y':
            continue
        if next_choice == 'n':
            break


if __name__ == "__main__":
    while True:
        selected_mode = input("choose a mode (D, V, G, M), or press E to exit: ").lower()
        if selected_mode == 'd':
            dictionary_mode()
        elif selected_mode == 'e':
            break


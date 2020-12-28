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

def vocabulary_trainer_mode():
    dictionary = Dictionary("words.txt")
    print("in this mode, you have to translate given vocabulary. First you will decide which language to translate from. If you want to exit, just press E")
    chosen_language = input("Do you want to translate German words (G) or English words (E)").lower()
    while True:
        if chosen_language == 'g':
            word_to_translate = dictionary.random_german_word()
            user_translation = input(f'what is the English translation of {word_to_translate}?')
            if user_translation == dictionary.german_to_english(word_to_translate):
                print("Correct!")
            elif user_translation == 'E':
                break
            else:
                print(f'This was not the correct translation. The correct translation is: {dictionary.german_to_english(word_to_translate)}')
        elif chosen_language == 'e':
            word_to_translate = dictionary.random_english_word()
            user_translation = input(f'what is the German translation of {word_to_translate}?')
            if user_translation == dictionary.english_to_german(word_to_translate):
                print("Correct!")
            elif user_translation == 'E':
                break
            else:
                print(f'this was not the correct translation. The correct translation is: {dictionary.english_to_german(word_to_translate)}')
     


if __name__ == "__main__":
    while True:
        selected_mode = input("choose a mode (D, V, G, M), or press E to exit: ").lower()
        if selected_mode == 'd':
            dictionary_mode()
        elif selected_mode == 'v':
            vocabulary_trainer_mode()
        elif selected_mode == 'e':
            break


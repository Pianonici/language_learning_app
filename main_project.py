from dictionary import Dictionary
import random
from user_progress import UserProgress

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
    print('''
    In this mode, you have to translate given vocabulary. 
    First you have to provide your username in order to save your progress. 
    Then you will decide which language to translate from. 
    While translating, if you want to exit, just press E.
    ''')
    user_name = input('Username: ')
    user_progress = UserProgress(user_name, dictionary._dictionary_german_to_english)
    user_progress.show_statistics_to_user()
    chosen_language = input("Do you want to translate German words (G) or English words (E) or random (R)").lower()
    while True:
        lowest_score_list = user_progress.get_lowest_score_list()
        random.shuffle(lowest_score_list)
        while lowest_score_list:
            german_word, english_word = lowest_score_list.pop()

            if chosen_language == 'r':
                language = random.choice(['g', 'e'])
            else:
                language = chosen_language

            if language == 'g':
                user_translation = input(f'what is the English translation of {german_word}?')
                if user_translation == english_word:
                    user_progress.add_point(german_word, english_word)
                    print("Correct!")
                elif user_translation == 'E':
                    user_progress.save_progress()
                    user_progress.show_statistics_to_user()
                    return
                else:
                    user_progress.subtract_point(german_word, english_word)
                    print(f'This was not the correct translation. The correct translation is: {english_word}')
            elif language == 'e':
                user_translation = input(f'what is the German translation of {english_word}?')
                if user_translation == german_word:
                    user_progress.add_point(german_word, english_word)
                    print("Correct!")
                elif user_translation == 'E':
                    user_progress.save_progress()
                    user_progress.show_statistics_to_user()
                    return
                else:
                    user_progress.subtract_point(german_word, english_word)
                    print(f'this was not the correct translation. The correct translation is: {german_word}')



if __name__ == "__main__":
    while True:
        selected_mode = input("choose a mode (D, V, G, M), or press E to exit: ").lower()
        if selected_mode == 'd':
            dictionary_mode()
        elif selected_mode == 'v':
            vocabulary_trainer_mode()
        elif selected_mode == 'e':
            break


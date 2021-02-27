from dictionary import Dictionary
from user_progress import UserProgress

import random


def dictionary_mode():
    dictionary = Dictionary("words.txt")
    while True:
        chosen_language = input(
            "Would you like to translate from German to English (press GE) or from English to German (press EG)? ")
        if chosen_language == 'GE':
            word_to_translate = input("which word do you want to translate? ")
            translate_result = (
                dictionary.german_to_english(word_to_translate))  # returns None if the word is not in the dictionary
            if translate_result is not None:
                print(translate_result)
            else:
                print("The word you want to translate is not in the dictionary.")
        if chosen_language == 'EG':
            word_to_translate = input("which word do you want to translate? ")
            translate_result = (
                dictionary.english_to_german(word_to_translate))  # returns None if the word is not in the dictionary
            if translate_result is not None:
                print(translate_result)
            else:
                print("The word you want to translate is not in the dictionary.")
        next_choice = input("Do you want to translate another word (Y/N)? ").lower()
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
    While translating, if you want to exit, just type "exit".
    ''')
    user_name = input('Username: ')  # to save the users' progress

    # the dictionary_german_to_english is needed to track the user progress for each word
    user_progress = UserProgress(user_name, dictionary.dictionary_german_to_english)

    user_progress.show_statistics_to_user()
    chosen_language = input("Do you want to translate German words (G) or English words (E) or random (R)? ").lower()
    while True:

        # Get list of words with the lowest score and randomize the order.
        # Each element of the list is a tuple of (German word, English word)
        lowest_score_list = user_progress.get_lowest_score_list()
        random.shuffle(lowest_score_list)

        # Go through each word of the list and ask the user to translate it.
        while lowest_score_list:

            # Pops a tuple from the randomized list, which the user then has to translate
            german_word, english_word = lowest_score_list.pop()

            if chosen_language == 'r':
                language = random.choice(['g', 'e'])
            else:
                language = chosen_language

            if language == 'g':
                user_translation = input(f'what is the English translation of {german_word}? ')
                if user_translation == english_word:
                    user_progress.add_point(german_word, english_word)
                    print("Correct!")
                # User specified they would like to exit.
                elif user_translation == 'exit':
                    user_progress.save_progress()
                    user_progress.show_statistics_to_user()
                    return
                else:
                    user_progress.subtract_point(german_word, english_word)
                    print(f'This was not the correct translation. The correct translation is: {english_word}')
            elif language == 'e':
                user_translation = input(f'what is the German translation of {english_word}? ')
                if user_translation == german_word:
                    user_progress.add_point(german_word, english_word)
                    print("Correct!")
                # User specified they would like to exit.
                elif user_translation == 'exit':
                    user_progress.save_progress()
                    user_progress.show_statistics_to_user()
                    return
                else:
                    user_progress.subtract_point(german_word, english_word)
                    print(f'this was not the correct translation. The correct translation is: {german_word}')


def grammar_mode():
    print('''
     In this mode, you can practice the conjugation of the verb "to be" in German.
     ''')
    be_is = {"Ich": "bin", "Du": "bist", "Er": "ist", "Sie": "ist", "Es": "ist"}
    be_are = {"Wir": "sind", "Ihr": "seid", "Sie": "sind"}
    while True:
        sentences = input('Please write a text that consists of several sentences '
                          'only using a pronoun and the verb "to be" in German: \n')
        # .split(".") returns a list of sentences separated by "."
        list_of_sentences = [sentence for sentence in sentences.split(".") if sentence.strip()]  # omit empty sentences
        for sentence in list_of_sentences:
            # .split() returns a list of words in the sentence. The first word must be the pronoun, the second word
            # must be the verb.
            pronoun = str(sentence.split()[0]).capitalize()
            verb = str(sentence.split()[1])
            # " ".join(sentence.split()[2:]) takes a list of all the words after the verb and combines them into a
            # string, putting a " " between the elements
            remainder_of_sentence = " ".join(sentence.split()[2:])
            if pronoun in be_is and verb == be_is[pronoun]:
                print('Your conjugation of the verb "to be" was correct!')
            elif pronoun in be_are and verb == be_are[pronoun]:
                print('Your conjugation of the verb "to be" was correct!')
            elif pronoun in be_is and verb != be_is[pronoun]:
                print(
                    f'Your conjugation of the verb "to be" was incorrect. The correct conjugation is "{pronoun} '
                    f'{be_is[pronoun]} {remainder_of_sentence}".')
            elif pronoun in be_are and verb != be_are[pronoun]:
                print(
                    f'Your conjugation of the verb "to be" was incorrect. The correct conjugation is "{pronoun} '
                    f'{be_are[pronoun]} {remainder_of_sentence}".')
            else:
                print('Incorrect input. The first word should be a pronoun and the second one a form '
                      'of "to be" in German.')
        next_choice = input("Do you want to practice another sentence (Y/N)? ").lower()
        if next_choice == "y":
            continue
        if next_choice == "n":
            break


def mad_libs_game_mode():
    print('''
     This mode is a phrasal word game.
     You do not have to provide any input. 
     ''')
    user_name = input('Username: ')
    while True:
        dictionary = Dictionary("words.txt")
        # the dictionary_german_to_english is needed to track the user progress for each word
        user_progress = UserProgress(user_name, dictionary.dictionary_german_to_english)
        # known_words are English words with a score of at least 5
        known_words = user_progress.get_known_words_list()
        random.shuffle(known_words)

        # Categorize known words by part of speech.
        list_known_nouns = []
        list_known_adj = []
        list_known_verbs = []
        for element in known_words:
            if dictionary.is_noun(element):
                list_known_nouns.append(element)
            if dictionary.is_adjective(element):
                list_known_adj.append(element)
            if dictionary.is_verb(element):
                list_known_verbs.append(element)

        # Fill in lists with random words if needed.
        while len(list_known_nouns) < 2:
            list_known_nouns.append(dictionary.random_english_noun())
        random.shuffle(list_known_nouns)
        while len(list_known_adj) < 3:
            list_known_adj.append(dictionary.random_english_adjective())
        random.shuffle(list_known_adj)
        while len(list_known_verbs) < 1:
            list_known_verbs.append(dictionary.random_english_verb())
        random.shuffle(list_known_verbs)

        # Fix determiner if the word starts with a vowel.
        determiner1 = 'an' if list_known_nouns[0][0] in 'aeiou' else 'a'
        determiner2 = 'an' if list_known_adj[1][0] in 'aeiou' else 'a'
        determiner3 = 'an' if list_known_adj[2][0] in 'aeiou' else 'a'

        phrasal_template = f'A unicorn is nothing like {determiner1} {list_known_nouns[0]}. ' \
                           f'They are {list_known_adj[0]} creatures. \n' \
                           f'Some have {determiner2} {list_known_adj[1]} mane of hair and others have {determiner3} ' \
                           f'{list_known_adj[2]} {list_known_nouns[1]} on their head. ' \
                           f'I would love {list_known_verbs[0]} a unicorn one day.'

        print(phrasal_template)

        next_choice = input("Do you want to see more phrases (Y/N)? ").lower()
        if next_choice == "y":
            continue
        else:
            break


# this is where the program starts execution
if __name__ == "__main__":
    while True:
        print('''
        In this Language Learning App, you can choose between four different modes:
        the Dictionary mode (D),
        the Vocabulary Trainer mode (V), 
        the Grammar mode(G), 
        the Mad Libs Game (M)
        ''')

        selected_mode = input('choose a mode (D, V, G, M), or type "exit" to exit: ').lower()
        if selected_mode == 'd':
            dictionary_mode()
        elif selected_mode == 'v':
            vocabulary_trainer_mode()
        elif selected_mode == 'g':
            grammar_mode()
        elif selected_mode == 'm':
            mad_libs_game_mode()
        elif selected_mode == 'exit':
            break

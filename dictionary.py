import random


class Dictionary(object):

    def __init__(self, file_name):
        # open a file, read the file, using the 'utf8' character set which includes 'Umlaute' (ä,ö,ü)
        f = open(file_name, 'r', encoding='utf8')
        lines = f.readlines()

        # creating dictionaries for both directions (English-German, German-English)
        self._dictionary_german_to_english = {}
        self._dictionary_english_to_german = {}

        # creating a dictionary to keep track of the part of speech of English words (needed for the mad-libs game)
        self._dictionary_english_to_part_of_speech = {}

        # map parts of speech to a list of English words
        self._dictionary_part_of_speech_to_english = {"(noun)": [], "(adj.)": [], "(verb)": []}

        # going through each line of the file
        for line in lines:
            line_elements = line.split(
                ', ')  # .split(', ') returns a list in the form of ["German word", "(part of speech)", "English word"]
            german_word = line_elements[0]
            part_of_speech = line_elements[1]
            english_word = line_elements[2].strip()  # .strip() in order to remove whitespaces at the end of the line
            self._dictionary_german_to_english[german_word] = english_word
            self._dictionary_english_to_german[english_word] = german_word
            self._dictionary_english_to_part_of_speech[english_word] = part_of_speech
            self._dictionary_part_of_speech_to_english[part_of_speech].append(english_word)

        f.close()

    # The following 2 functions are used to get the correct translations of words
    def german_to_english(self, word):
        if word in self._dictionary_german_to_english:
            return self._dictionary_german_to_english[word]
        else:
            return None

    def english_to_german(self, word):
        if word in self._dictionary_english_to_german:
            return self._dictionary_english_to_german[word]
        else:
            return None

    # The following 2 functions are used to get random words (keys) from the dictionary
    def random_german_word(self):
        return random.choice(list(self._dictionary_german_to_english.keys()))

    def random_english_word(self):
        return random.choice(list(self._dictionary_english_to_german.keys()))

    # the next three functions check for the part of speech of a word
    def is_noun(self, word):
        if self._dictionary_english_to_part_of_speech[word] == "(noun)":
            return True
        else:
            return False

    def is_adjective(self, word):
        if self._dictionary_english_to_part_of_speech[word] == "(adj.)":
            return True
        else:
            return False

    def is_verb(self, word):
        if self._dictionary_english_to_part_of_speech[word] == "(verb)":
            return True
        else:
            return False

    # the next three functions give us a random English word of a given part of speech category
    # the values of _dictionary_part_of_speech_to_english are lists and random.choice gives us
    # a random entry from that list
    def random_english_noun(self):
        return random.choice(self._dictionary_part_of_speech_to_english["(noun)"])

    def random_english_adjective(self):
        return random.choice(self._dictionary_part_of_speech_to_english["(adj.)"])

    def random_english_verb(self):
        return random.choice(self._dictionary_part_of_speech_to_english["(verb)"])

import random

class Dictionary(object):

    def __init__(self, file_name):
        f = open(file_name, 'r', encoding='utf8')
        lines = f.readlines()
        self._dictionary_german_to_english = {}
        self._dictionary_english_to_german = {}
        self._dictionary_english_to_part_of_speech = {}
        self._dictionary_part_of_speech_to_english = {"(noun)": [], "(adj.)": [], "(verb)": []}
        for line in lines:
            line_elements = line.split(', ')
            self._dictionary_german_to_english[line_elements[0]] = line_elements[-1].strip()
            self._dictionary_english_to_german[line_elements[-1].strip()] = line_elements[0]
            self._dictionary_english_to_part_of_speech[line_elements[-1].strip()] = line_elements[1]
            self._dictionary_part_of_speech_to_english[line_elements[1]].append(line_elements[-1].strip())
            
        f.close()

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

    def random_german_word(self):
        random_entry = random.choice(list(self._dictionary_german_to_english.items()))
        return random_entry[0]

    def random_english_word(self):
        random_entry = random.choice(list(self._dictionary_english_to_german.items()))
        return random_entry[0]

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

    def random_english_noun(self):
        return random.choice(self._dictionary_part_of_speech_to_english["(noun)"])

    def random_english_adjective(self):
        return random.choice(self._dictionary_part_of_speech_to_english["(adj.)"])

    def random_english_verb(self):
        return random.choice(self._dictionary_part_of_speech_to_english["(verb)"])

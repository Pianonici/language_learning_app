import random

class Dictionary(object):
    
    def __init__(self, file_name):
        f = open(file_name, 'r', encoding='utf8')
        lines = f.readlines()
        self._dictionary_german_to_english = {}
        self._dictionary_english_to_german = {}
        self.speech = {}  # fuer noun, verb, adj?
        for line in lines:
            line_elements = line.split(', ')
            self._dictionary_german_to_english[line_elements[0]] = line_elements[-1].strip()
            self._dictionary_english_to_german[line_elements[-1].strip()] = line_elements[0]
            self.speech = line_elements[1]  # fuer noun, verb, adj?
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

    def noun(self):
        if self.speech == "(noun)":
            random_noun = random.choice(list(self._dictionary_english_to_german.items()))
            return random_noun[0]

    def adjective(self):
        if self.speech == "(adj.)":
            random_adj = random.choice(list(self._dictionary_english_to_german.items()))
            return random_adj[0]

    def verb(self):
        if self.speech == "(verb)":
            random_verb = random.choice(list(self._dictionary_english_to_german.items()))
            return random_verb[0]







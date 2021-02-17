from dictionary import Dictionary


def madlibsgame_mode():
    dictionary = Dictionary("words.txt")
    noun = dictionary.noun()
    adjective = dictionary.adjective()
    verb = dictionary.verb()
    print("A unicorn is nothing like a", noun, ". They are", adjective, "creatures. Some have a", adjective,
          "mane of hair and others have a", adjective, noun, "on their head. I would love to",
          verb, "a unicorn one day.")


print(madlibsgame_mode())


def adjective(self):
    words = (list(self._dictionary_english_to_german.items()))
    adj = [word for word in words if self.speech == "(adj.)"]
    return random.choice(adj)

def adjective(self):
    if self.speech == "(adj.)":
        random_adj = random.choice(list(self._dictionary_english_to_german.items()))
        return random_adj[0]


def verb(self):
    if self.speech == "(verb)":
        random_verb = random.choice(list(self._dictionary_english_to_german.items()))
        return random_verb[0]



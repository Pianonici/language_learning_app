from dictionary import Dictionary

#verschiedene versuche gesichert

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
    words = (list(self.dictionary_english_to_german.items()))
    adj = [word for word in words if self.speech == "(adj.)"]
    return random.choice(adj)

def adjective(self):
    if self.speech == "(adj.)":
        random_adj = random.choice(list(self.dictionary_english_to_german.items()))
        return random_adj[0]


class Words(Dictionary):

    def __init__(self, file_name):
        super().__init__(file_name)

    def noun(self):
        if self.speech == "(noun)":
            noun = list(Words.random_english_word(self))
            random_noun = random.choice(noun)
            return random_noun[0]
        else:
            pass


    def adj(self):
        if self.speech == "(adj.)":
            adj = list(Words.random_english_word(self))
            random_adj = random.choice(adj)
            return random_adj[0]
        else:
            pass

    def verb(self):
        if self.speech == "(verb)":
            verb = list(Words.random_english_word(self))
            random_verb = random.choice(verb)
            return random_verb[0]
        else:
            pass




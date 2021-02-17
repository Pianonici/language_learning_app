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


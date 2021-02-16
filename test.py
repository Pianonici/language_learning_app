def grammar_mode():
    print('''
     In this mode, you can practice the conjunction of the verb to be.
     To practice that, please write several sentences only using the verb "to be" and pronouns.
     ''')
    be_is = {"ich": "bin", "du": "bist", "er": "ist", "sie": "ist", "es": "ist"}
    be_are = {"wir": "sind", "ihr": "seid", "sie": "sind"}
    while True:
        sentences = input("Please write: ")
        pronoun = str(sentences.split()[0])
        verb = str(sentences.split()[1])
        if pronoun in be_is and verb == be_is[pronoun]:
            print("correct")
        elif pronoun in be_are and verb == be_are[pronoun]:
            print("correct")
        elif pronoun in be_are and verb != be_are[pronoun]:
            print("incorrect")
        elif pronoun in be_is and verb != be_is[pronoun]:
            print("incorrect")
        else:
            print("false")
        next_choice = input("Do you want to practice another sentence? (Y/N)")
        if next_choice == 'y':
            continue
        if next_choice == 'n':
            break


print(grammar_mode())

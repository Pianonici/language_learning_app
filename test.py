print('''
 In this mode, you can practice the conjunction of the verb to be.
 To practice that, please write several sentences only using the verb "to be" and pronouns.
 ''')
#def grammar_mode():
be = {"ich": "bin", "du": "bist", "er": "ist", "sie": "ist", "es": "ist",
      "wir": "sind", "ihr": "seid", "sie": "sind"}
#be_ = ("Ich bin", "Du bist", "Er ist", "Sie ist", "Es ist", "Wir sind", "Ihr seid", "Sie sind")
sentences = input("Please write several sentences only using pronouns and the verb to be, seperated by dots: ")
#idee: schauen ob key value paar so in dictionary steht oder nicht
for x in sentences.split():
    if x in be.keys():
        for y in sentences.split():
            if y in be.values():
                print("correct")
            else:
                print("wrong use of to be")

from pathlib import Path
from copy import copy


class UserProgress(object):
    def __init__(self, user_name, german_to_english_dictionary):
        self._filepath = Path(
            f'user_progress_{user_name}.txt')  # we need this for the filepath because we are creating a file
        self._word_to_score = {}
        self._score_to_words = {}
        lowest_score = 0

        # Check if the file already exists. If it does, read the user progress
        if self._filepath.is_file():
            # Open the file if it already exists; 'utf8'is a character set that includes 'Umlaute' (ä,ö,ü)
            file = self._filepath.open('r', encoding='utf8')
            # Each line is a string that looks like: "Abend, evening, -1"
            lines = file.readlines()  # gives us a list of lines
            for line in lines:
                # ignore empty lines
                if line.strip() != "":
                    line_elements = line.split(', ')  # gives us a list ["german word", "english word", "score"]
                    german_word = line_elements[0]
                    english_word = line_elements[1]
                    score = int(line_elements[2])
                    if score < lowest_score:
                        lowest_score = score
                    combined_word = (german_word, english_word)  # creating tuple
                    self._word_to_score[combined_word] = score  # map tuple to score
                    if score in self._score_to_words:  # if score already exists
                        self._score_to_words[score].append(combined_word)
                        # appending the tuple to the list of words with same score
                    else:
                        self._score_to_words[score] = [combined_word]
                        # if it's the first score with that score, map the score to a list of
                        # tuples with the given tuple as the first element of that list
            file.close()

        # if you do not already have user progress for a word, map it to a score of -1
        # using the dictionary, set score of all new words to be one less than the worst score
        for entry in german_to_english_dictionary.items():
            # .items() returns a list consisting of tuples (all combined words)
            if entry not in self._word_to_score:
                self._word_to_score[entry] = lowest_score - 1
                if lowest_score - 1 not in self._score_to_words:
                    self._score_to_words[lowest_score - 1] = []
                self._score_to_words[lowest_score - 1].append(entry)

    def add_point(self, german_word, english_word):
        combined_word = (german_word, english_word)
        if combined_word in self._word_to_score:
            current_score = self._word_to_score[combined_word]
            self._word_to_score[combined_word] += 1
            self._score_to_words[current_score].remove(combined_word)
            if self._score_to_words[current_score] == []:  # if the tuple was the last word of the list
                self._score_to_words.pop(current_score)  # delete the key-value-pair
            if current_score + 1 in self._score_to_words:
                # append the tuple to the new score list if list already exists
                self._score_to_words[current_score + 1].append(combined_word)
            else:
                # if new score list does not already exist, create new list
                self._score_to_words[current_score + 1] = [combined_word]
                
    def subtract_point(self, german_word, english_word):
        combined_word = (german_word, english_word)
        if combined_word in self._word_to_score:
            current_score = self._word_to_score[combined_word]
            self._word_to_score[combined_word] -= 1
            self._score_to_words[current_score].remove(combined_word)
            if self._score_to_words[current_score] == []:  # if the tuple was the last word of the list
                self._score_to_words.pop(current_score)  # delete the key-value-pair
            if current_score - 1 in self._score_to_words:
                # append the tuple to the new score list if list already exists
                self._score_to_words[current_score - 1].append(combined_word)
            else:
                # if new score list does not already exist, create new list
                self._score_to_words[current_score - 1] = [combined_word]
                
    # write the user's progress to a file
    def save_progress(self):
        file = self._filepath.open('w+', encoding='utf8')
        for combined_word, score in self._word_to_score.items():
            # .items() goes through all elements in the dictionary and gives us tuples.
            # Each element looks like: ((Abend, evening), -1)
            german_word = combined_word[0]
            english_word = combined_word[1]
            file.write(f'{german_word}, {english_word}, {score}\n')
        file.close()

    def show_statistics_to_user(self):
        # dictionary to show how many words have which star-count based on word's score
        star_count = {
            0: 0,
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            "total": 0
        }
        for score in self._word_to_score.values():
            if score < 0:
                star_count[0] += 1
            elif score < 2:
                star_count[1] += 1
                star_count["total"] += 1
            elif score < 4:
                star_count[2] += 1
                star_count["total"] += 2
            elif score < 6:
                star_count[3] += 1
                star_count["total"] += 3
            elif score < 8:
                star_count[4] += 1
                star_count["total"] += 4
            else:
                star_count[5] += 1
                star_count["total"] += 5

        if star_count["total"] < 100:
            print(f'''Keep studying your vocabulary. Your current STARCOUNT is {star_count["total"]} out of 500!''')
        elif star_count["total"] < 300:
            print(f'''You are on the right track. Your current STARCOUNT is {star_count["total"]} out of 500!''')
        elif star_count["total"] < 500:
            print(f'''You have been doing a good job studying your vocabulary. Your current STARCOUNT is
                  {star_count["total"]} out of 500!''')
        else:
            print(f'''Excellent! Your current STARCOUNT is {star_count["total"]} out of 500!''')

        print(f'''
        Words with 5 stars: {star_count[5]}
        Words with 4 stars: {star_count[4]}
        Words with 3 stars: {star_count[3]}
        Words with 2 stars: {star_count[2]}
        Words with 1 star: {star_count[1]}
        Words that don't have any star yet: {star_count[0]}
            ''')

    # return a copy of the list of words with the lowest score
    # we have to use a copy, otherwise when the user pops from the list,
    # when they have to translate words with the lowest score,
    # the list would be entirely deleted after they translate the last word.
    # But we don't want the word to be deleted from the original list,
    # so they get a copy of the list which is fine to be deleted.
    def get_lowest_score_list(self):
        lowest_score = min(self._score_to_words.keys())
        return copy(self._score_to_words[lowest_score])

    # storing words with a total score of at least 5 in a list.
    def get_known_words_list(self):  # for mad_libs game
        known_words = []
        for combined_word, score in self._word_to_score.items():
            # .items() goes through all elements in the dictionary and gives us tuples.
            # Each element looks like: ((Abend, evening), -1)
            if score >= 5:
                english_word = combined_word[1]
                known_words.append(english_word)
        return known_words

        # automatically save user progress if user exits the mode

    def __del__(self):  # __del__is called when the object is done being used
        self.save_progress()

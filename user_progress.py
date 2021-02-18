from pathlib import Path
from copy import copy
import random

class UserProgress(object):
    def __init__(self, user_name, german_to_english_dictionary):
        self._filepath = Path(f'user_progress_{user_name}.txt') 
        self._word_to_score = {}
        self._score_to_words = {}
        lowest_score = 0
        if self._filepath.is_file():
            file = self._filepath.open('r', encoding='utf8')
            # Abend, evening, -1 
            lines = file.readlines()
            for line in lines:
                if line.strip():
                    line_elements = line.split(', ')
                    german_word = line_elements[0]
                    english_word = line_elements[1]
                    score = int(line_elements[-1])
                    if score < lowest_score: 
                        lowest_score = score
                    combined_word = (german_word, english_word)
                    self._word_to_score[combined_word] = score
                    if score in self._score_to_words:
                        self._score_to_words[score].append(combined_word)
                    else:
                        self._score_to_words[score] = [combined_word]
            file.close()
        for entry in german_to_english_dictionary.items():
            if entry not in self._word_to_score:
                self._word_to_score[entry] = lowest_score -1
                if lowest_score -1 not in self._score_to_words:
                    self._score_to_words[lowest_score -1] = []
                self._score_to_words[lowest_score -1].append(entry) 
            
        
        #Take dictionary as an argument, set score of all new words to be one less than the worst score

    def add_point(self, german_word, english_word):
        combined_word = (german_word, english_word)
        if combined_word in self._word_to_score:
            current_score = self._word_to_score[combined_word]
            self._word_to_score[combined_word] += 1
            self._score_to_words[current_score].remove(combined_word)
            if self._score_to_words[current_score] == []:
                self._score_to_words.pop(current_score)
            if current_score +1 in self._score_to_words:
                self._score_to_words[current_score +1].append(combined_word)
            else:
                self._score_to_words[current_score +1] = [combined_word]
    def subtract_point(self, german_word, english_word):
        combined_word = (german_word, english_word)
        if combined_word in self._word_to_score:
            current_score = self._word_to_score[combined_word]
            self._word_to_score[combined_word] -= 1
            self._score_to_words[current_score].remove(combined_word)
            if self._score_to_words[current_score] == []:
                self._score_to_words.pop(current_score)
            if current_score -1 in self._score_to_words:
                self._score_to_words[current_score -1].append(combined_word)
            else:
                self._score_to_words[current_score - 1] = [combined_word]
    
    def save_progress(self):
        file = self._filepath.open('w+', encoding='utf8')
        for combined_word, score in self._word_to_score.items():
            # ((Abend, evening), -1)
            file.write(f'{combined_word[0]}, {combined_word[1]}, {score}\n')
        file.close()
    
    def show_statistics_to_user(self):
        star_count = {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            4 : 0,
            5 : 0,
            "total" : 0
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
            print(f'''You have been doing a good job studying your vocabulary. Your current STARCOUNT is {star_count["total"]} out of 500!''')
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

    def get_lowest_score_list(self):
        lowest_score = min(self._score_to_words.keys())
        return copy(self._score_to_words[lowest_score])

    def get_known_words_list(self): #for mad_libs game
        known_words = []
        for combined_word, score in self._word_to_score.items():
            if score >= 5:
                known_words.append(combined_word[1])
        return known_words 


    def __del__(self):
        self.save_progress()
         
       

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

    def get_lowest_score_list(self):
        lowest_score = min(self._score_to_words.keys())
        return copy(self._score_to_words[lowest_score])
            
    def __del__(self):
        self.save_progress()
         
       

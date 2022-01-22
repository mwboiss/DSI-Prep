from collections import Counter

def word_count(word_lst):
    count_dict = Counter(word_lst)
    return count_dict

# given example 

import collections

def word_count(word_lst):
    
    count_of_words = collections.Counter(word_lst)
    return count_of_words
from collections import Counter

def five_most_common(string):
    
    punctuation = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    
    n_st = string.lower()
    print(n_st)
    for val in n_st:
        if val in punctuation:
            n_st = n_st.replace(val,'')
    print(n_st)
    word_count = Counter(n_st.split()).most_common(5)
    
    most_common = []
    
    for val in word_count:
        most_common.append(val[0])
    
    return most_common

sentence = 'The quick brown fox jumps over the lazy dog\'s tail.'
print('\n\n\n\n\n')
print(five_most_common(sentence))

# given example

# write import statement below
from collections import Counter

def five_most_common(string):
  '''
  Finds the five most common words in a string

  Parameters:
  ----------
  string: (str)

  Returns:
  ----------
  Returns the five most common words
  '''
  lower = string.lower()

  clean = lower.replace('.', '')
  clean = clean.replace('?', '')
  clean = clean.replace('!', '')
  clean = clean.replace(',', '')

  counts = Counter(clean.split())
  return [word for word, count in counts.most_common(5)]
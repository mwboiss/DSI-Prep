rand_paragraph = '''"New York City member-supported radio station WFUV named Free Yourself Up its New Dig, aka Album of the Week. On the album, the band "strives to empower and liberate in an age of turmoil," says FUV. "It’s a confident collection of songs that reflects the quartet’s nearly decade-and-a-half of music making. (cite nonsuch records announcement New York City member-supported radio station WFUV named Free Yourself Up its New Dig, aka Album of the Week. On the album, the band "strives to empower and liberate in an age of turmoil," says FUV. "It’s a confident collection of songs that reflects the quartet’s nearly decade-and-a-half of music making."'''

def get_clean_word_list(paragraph):
    to_remove = ['"', '(', ')', '.']
    cleaned = paragraph[:]
    for punc in to_remove:
        cleaned = cleaned.replace(punc, '')
    cleaned = cleaned.lower()
    return cleaned.split(' ')

def word_count_dict(paragraph):
    word_list = get_clean_word_list(paragraph)
    
    # clean up double quotes, lowercase
    for i, word in enumerate(word_list):
        word_list[i] = word.lower()

    word_count_dict = {} # dict()

    for word in word_list:
        if word not in word_count_dict.keys():
            word_count_dict[word] = 0
        word_count_dict[word] += 1

    return word_count_dict

# Here you use .items() to traverse the dict you've made
for word, count in word_count_dict(rand_paragraph).items():
    print(f'{word}: {count}')
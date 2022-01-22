str1 = "Hello there!"
# prints empty keys
def letter_idx_1(str1):
    n_str = str1.lower()
    v_lst = [[],[],[],[],[],[]]
    v_dic = {'a':v_lst[0],'e':v_lst[1],'i':v_lst[2],'o':v_lst[3],'u':v_lst[4],'y':v_lst[5]}
    for idxv, vow in enumerate("aeiouy"):
        for idxc, char in enumerate(n_str):
            if char == vow:
               v_lst[idxv].append(idxc)
    return v_dic
# This one worked
def letter_idx_2(str1):
    n_str = str1.lower()
    v_dic = dict()
    for idxv, vow in enumerate("aeiouy"):
        for idxc, char in enumerate(n_str):
            if char == vow:
                if vow in v_dic:
                    v_dic[vow].append(idxc)
                else:
                    v_dic[vow] = [idxc]
    return v_dic

print(letter_idx_1(str1))
print(letter_idx_2(str1))

# example given

def letter_idx(word):
    # This is the vowel index accumulator
    vowel_dict = {}

    # Use 'enumerate' since both index and character are used
    # Use 'word.lower()' since the function should be case-insensitive
    for idx, char in enumerate(word.lower()):
        if char in "aeiouy":
            # If the vowel is already in the dictionary, append the index
            if char in vowel_dict:
                vowel_dict[char].append(idx)
            # Otherwise, initialize the dictionary key with a new list containing the index
            else:
                vowel_dict[char] = [idx]

    return vowel_dict

# another example

def letter_idx(word):
    vowel_dict = {}

    for idx, char in enumerate(word.lower()):
        if char in "aeiouy":
            vowel_dict[char] = vowel_dict.get(char, []) + [idx]

    return vowel_dict
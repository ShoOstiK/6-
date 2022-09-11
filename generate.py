import random
from collections import defaultdict,Counter
import pickle

def decode_object(obj):
    return pickle.loads(obj)

def select_first_prefix(dict_of_tokens,prefix_start):
    if (prefix_start==None):
        first_prefix=random.choice(list(dict_of_tokens.keys()))
        return first_prefix
    else:
        for elem in dict_of_tokens:
            if prefix_start==' '.join(list(elem)):
                return elem




def text_generation(obj,length,prefix):

    dict_of_tokens = decode_object(obj)
    first_prefix=(select_first_prefix(dict_of_tokens,prefix))
    sequence = list(first_prefix)

    for idx in range(length):
        random_word=dict_of_tokens[first_prefix].keys()
        random_word=random.choice(list(random_word))
        if random_word == 'EOS':
            sequence+=['.']
            first_prefix=random.choice(list(dict_of_tokens.keys()))

        else:
            sequence+=[random_word]
            first_prefix=first_prefix[1:]+(random_word,)
    return ' '.join(sequence)











from functools import reduce
import re
from string import punctuation
from random import choice
from collections import defaultdict,Counter
import pickle

def preprocessing(file=None):
    file = open('data.txt').readlines()
    file = list(filter(lambda x: x != '\n', file))
    file = [row.replace('\n', '').lower() for row in file]
    file = [row.replace('\xa0', '') for row in file]
    file = [''.join(list((filter(lambda item: item not in punctuation + '«»–', elem)))) for elem in file]

    for ind in range(len(file)):
        file[ind] = re.sub("[q|w|e|r|t|y|u|i|o|p|a|s|d|f|g|h|j|k|l|z|x|c|v|b|n|m]", "", file[ind])

    file=tokenization(corpus=file)

    unique_tokens = set(reduce(lambda x, y: x + y, file))

    token_to_num = {elem: ind for ind, elem in enumerate(unique_tokens)}

    num_to_token = {ind: elem for ind, elem in enumerate(unique_tokens)}


    return file

def tokenization(corpus=None):
    for ind, line in enumerate(corpus):
        corpus[ind] = re.split(r' ', corpus[ind])


    return corpus


def n_grams(file, model, n=1):
    for num, row in enumerate(file):
        if len(row) < n:
            continue

        for idx in range(-1, len(row) - n + 1):

            if idx == -1:
                prefix = ['BOS'] + row[idx + 1:idx + (n)]
                try:
                    model[tuple(prefix)][row[idx + n]] += 1
                except:
                    model[tuple(prefix)]['EOS'] += 1
            else:
                prefix = row[idx:idx + n]
                try:
                    model[tuple(prefix)][row[idx + n]] += 1
                except:
                    model[tuple(prefix)]['EOS'] += 1

    dict_of_tokens = set_probabilities(model)

    return dict_of_tokens


def set_probabilities(dictionary=None):
    for prefix in dictionary:

        all_count = sum(dictionary[prefix].values())

        for word in dictionary[prefix]:
            dictionary[prefix][word] = dictionary[prefix][word] / all_count
    return dictionary

def encode_object(obj):
    return pickle.dumps(obj)

def fit_model(input_dir=None,model=None):
    tokenize_text=preprocessing(input_dir)
    dict_of_tokens=n_grams(tokenize_text,model,n=1)
    encoded_dict=encode_object(dict_of_tokens)

    return encoded_dict
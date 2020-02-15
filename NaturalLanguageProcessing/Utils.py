from collections import Counter
import re

TERMINATION_MARKS = ['.', '?', '!', ';']


def prepare_data(path):
    with open(path) as f:
        txt = f.read()

    words_list = convert_text_to_list(txt)
    counter = Counter(words_list)

    return words_list, counter

def prepare_sentences(path):
    with open(path) as f:
        txt = f.read()
    sentence_list = convert_to_sentence_list(txt)

    return sentence_list



def convert_text_to_list(txt):
    # txt = re.sub('[^a-zåäö\']+', " ", txt)
    txt = re.sub('[^a-zåäö.?!;\']+', " ", txt)  # we keep the termination marks
    words_list = list(txt.split())

    return words_list

def convert_to_sentence_list(txt):
    pass


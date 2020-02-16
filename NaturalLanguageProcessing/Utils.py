from collections import Counter
import re


def prepare_data(path):
    with open(path) as f:
        txt = f.read()

    sentences_list = convert_text_to_sentences_list(txt)
    counter = Counter(convert_text_to_words_list(txt))

    return sentences_list, counter


def convert_text_to_words_list(txt):
    txt = re.sub('[^a-zåäö\']+|(&quot;)+', " ", txt)
    words_list = list(txt.split())

    return words_list


def convert_text_to_sentences_list(txt):
    sentences = []
    txt = re.sub('[^a-zåäö.?!;\']+|(&quot;)+', " ", txt)

    for sentence_str in re.split("[.!?;]([^a-zåäö]|$)", txt):
        sentence_str = sentence_str.strip()

        if sentence_str:
            sentences.append([''] + sentence_str.split())

    return sentences

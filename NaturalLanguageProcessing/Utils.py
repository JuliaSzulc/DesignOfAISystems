from collections import Counter
import re


def prepare_data(path):
    lines = []
    with open(path) as f:
        for line in f:
            lines.append(line)

    sentences_words_list = convert_text_lines_to_sentences_list(lines)

    return sentences_words_list


def convert_text_to_words_list(txt):
    txt = re.sub('[^a-zåäö\']+|(&quot;)+', " ", txt)
    words_list = [''] + list(txt.split())

    return words_list


def convert_text_to_sentences_list(txt):
    sentences = []
    txt = re.sub('[^a-zåäö.?!;\']+|(&quot;)+', " ", txt)

    for sentence_str in re.split("[.!?;]([^a-zåäö]|$)", txt):
        sentence_str = sentence_str.strip()

        if sentence_str:
            sentences.append([''] + sentence_str.split())

    return sentences


def convert_text_lines_to_sentences_list(lines):
    sentences = []

    for line in lines:
        sentence = re.sub('[^a-zåäö\']+|(&quot;)+', " ", line)
        sentence = sentence.strip()

        if sentence:
            sentences.append([''] + sentence.split())

    return sentences

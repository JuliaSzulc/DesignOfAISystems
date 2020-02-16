from collections import Counter
from itertools import chain
from numpy import log, exp


class LanguageModel:
    def __init__(self, sentences_list):
        self.pairs_counter = Counter()
        self.words_counter = Counter()
        self.penalty = 0.001

        self.count_words(sentences_list)
        self.count_pairs(sentences_list)

    def count_words(self, sentences_list):
        words_list = list(chain(*sentences_list))
        self.words_counter = Counter(words_list + [''])

    def count_pairs(self, sentences_list):
        self.pairs_counter = Counter()

        for sentence in sentences_list:
            self.pairs_counter[('', sentence[0])] += 1

            for word1, word2 in zip(sentence, sentence[1:]):
                self.pairs_counter[(word1, word2)] += 1

    def calculate_probability(self, pair):
        if any(word not in self.words_counter for word in pair) or \
           pair not in self.pairs_counter:
            return self.penalty

        if pair[0] == '':
            return self.pairs_counter[pair] / self.words_counter[pair[1]]

        return self.pairs_counter[pair] / self.words_counter[pair[0]]

    def calculate_probability_of_sentence(self, sentence):
        total_log_probability = log(
            self.calculate_probability(('', sentence[0])))

        for word1, word2 in zip(sentence, sentence[1:]):
            total_log_probability += log(
                self.calculate_probability((word1, word2)))

        return exp(total_log_probability)

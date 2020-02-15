from collections import Counter
from itertools import chain


class Bigram:
    def __init__(self, sentences_list):
        self.pairs_counter = Counter()
        self.words_counter = Counter()

        self.count_words(sentences_list)
        self.count_pairs(sentences_list)

    def count_words(self, sentences_list):
        words_list = list(chain(*sentences_list))
        self.words_counter = Counter(words_list)

    def count_pairs(self, sentences_list):
        self.pairs_counter = Counter()

        for sentence in sentences_list:
            self.pairs_counter[('', sentence[0])] += 1

            for word1, word2 in zip(sentence, sentence[1:]):
                self.pairs_counter[(word1, word2)] += 1

    def calculate_probability(self, pair):
        if pair[0] == '':
            if pair[1] not in self.words_counter:
                return 0
            return self.pairs_counter[pair] / self.words_counter[pair[1]]

        if pair[0] not in self.words_counter:
            return 0
        return self.pairs_counter[pair] / self.words_counter[pair[0]]

    def calculate_probability_of_sentence(self, sentence):
        total_probability = self.calculate_probability(('', sentence[0]))

        for i in range(len(sentence) - 1):
            total_probability *= self.calculate_probability(
                (sentence[i], sentence[i + 1]))

        return total_probability

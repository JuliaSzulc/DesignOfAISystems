from collections import Counter

from Utils import TERMINATION_MARKS


class Bigram():
    def __init__(self, words_list):
        self.pairs_counter = Counter()
        self.words_counter = Counter()

        self.count_words(words_list)
        self.count_pairs(words_list)

    def count_words(self, words_list):
        filtered_list = [word for word in words_list if word not in TERMINATION_MARKS]
        self.words_counter = Counter(filtered_list)

    def count_pairs(self, words_list):
        self.pairs_counter = Counter()

        for i in range(len(words_list) - 1):
            word1 = words_list[i]
            word2 = words_list[i + 1]

            if word2 in TERMINATION_MARKS:
                continue

            if word1 in TERMINATION_MARKS:
                self.pairs_counter[word2] += 1
                continue

            self.pairs_counter[(word1, word2)] += 1

    def calculate_probability(self, pair):
        if not isinstance(pair, tuple):
            if pair not in self.words_counter:
                return 0
            return self.pairs_counter[pair] / self.words_counter[pair]

        if pair[0] not in self.words_counter:
            return 0
        return self.pairs_counter[pair] / self.words_counter[pair[0]]

    def calculate_probability_of_sentence(self, sentence):
        total_probability = self.calculate_probability(sentence[0])

        for i in range(len(sentence) - 1):
            total_probability *= self.calculate_probability(
                (sentence[i], sentence[i + 1]))

        return total_probability

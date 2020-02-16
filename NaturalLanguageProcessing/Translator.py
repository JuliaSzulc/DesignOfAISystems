from collections import Counter
from random import random
from itertools import chain


class Translator:
    def __init__(self, foreign_sentences, native_sentences, epochs=10):
        self.foreign_sentences = foreign_sentences
        self.native_sentences = native_sentences

        self.foreign_words = set(chain(*foreign_sentences))
        self.native_words = set(chain(*native_sentences))

        self.epochs = epochs

        self.translation_probs = {}  # [n][f]

        self.pseudo_counts = {}  # [n][f]
        self.foreign_counts = Counter()
        self.native_counts = Counter()

    def train(self):
        self.set_random_translation_probabilities()

        for i in range(self.epochs):
            self.reset_counts()

            for n_sentence, f_sentence in zip(self.native_sentences,
                                              self.foreign_sentences):
                for n_word in n_sentence:
                    for f_word in f_sentence:
                        self.update_counts(n_word, f_word,
                                           self.translation_probs[n_word][f_word])
            self.update_probabilities()
        self.print_results()

    def set_random_translation_probabilities(self):
        self.translation_probs = {n: {f: random() for f in self.foreign_words}
                                  for n in self.native_words}

    def reset_counts(self):
        self.pseudo_counts = {n: Counter() for n in self.native_words}
        self.foreign_counts = Counter()
        self.native_counts = Counter()

    def update_counts(self, n_word, f_word, translation_prob):
        self.native_counts[n_word] += translation_prob

        ratio = translation_prob / self.native_counts[n_word]

        self.pseudo_counts[n_word][f_word] += ratio
        self.foreign_counts[f_word] += ratio

    def update_probabilities(self):
        for f_word in self.foreign_words:
            for n_word in self.native_words:
                prob = self.pseudo_counts[n_word][f_word] / self.foreign_counts[f_word]
                self.translation_probs[n_word][f_word] = prob

    def print_results(self):
        for n_word, f_words in self.translation_probs.items():
            n_word = 'NULL' if not n_word else n_word
            print("\n {}:".format(n_word))
            for f_word, probability in f_words.items():
                f_word = 'NULL' if not f_word else f_word
                print("{}:  {:0.4f}".format(f_word, probability))

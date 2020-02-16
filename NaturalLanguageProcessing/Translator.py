from collections import Counter
from random import random
from itertools import chain


class Translator:
    def __init__(self, foreign_sentences, native_sentences):
        self.foreign_sentences = foreign_sentences
        self.native_sentences = native_sentences

        self.foreign_words = set(chain(*foreign_sentences))
        self.native_words = set(chain(*native_sentences))

        self.translation_probs = {}  # [n][f]

        self.pseudo_counts = {}  # [n][f]
        self.foreign_counts = Counter()
        self.native_counts = Counter()

    def train(self, epochs=10, printed_results='all', printed_words=[]):
        self.init_translation_probabilities_dict()

        for i in range(epochs):
            print("Epoch {}/{}".format(i+1, epochs))

            self.reset_counts()
            total_sentences = min(len(self.native_sentences),
                                  len(self.foreign_sentences))
            for n_sentence, f_sentence, s in zip(self.native_sentences,
                                                 self.foreign_sentences,
                                                 range(total_sentences)):
                print("Sentence {}/{}".format(s+1, total_sentences), end='\r')

                for n_word in n_sentence:
                    for f_word in f_sentence:
                        self.initialize_probability_if_needed(n_word, f_word)
                        self.update_counts(n_word, f_word,
                                           self.translation_probs[n_word][f_word])
            print('\n')
            self.update_probabilities()
            self.print_results(printed_results, printed_words)

    def initialize_probability_if_needed(self, n_word, f_word):
        if f_word not in self.translation_probs[n_word].keys():
            self.translation_probs[n_word][f_word] = random()

    def init_translation_probabilities_dict(self):
        self.translation_probs = {n: {} for n in self.native_words}

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
        f_len = len(self.foreign_words)

        for f_word, f in zip(self.foreign_words, range(f_len)):
            for n_word in [n for n in self.native_words if
                           f_word in self.translation_probs[n]]:
                print("Words: {}/{}".format(f + 1, f_len), end='\r')

                prob = self.pseudo_counts[n_word][f_word] / self.foreign_counts[f_word]
                self.translation_probs[n_word][f_word] = prob

    def print_results(self, printed_results='all', printed_words=[]):
        print('\n')

        for n_word, f_words in self.translation_probs.items():
            if len(printed_words) and n_word not in printed_words:
                continue

            n_word = 'NULL' if not n_word else n_word
            print("\n {}:".format(n_word))

            f_words_sorted = sorted(f_words.items(), reverse=True,
                                    key=lambda w: w[1])
            if printed_results != 'all':
                f_words_sorted = f_words_sorted[:printed_results]

            for f_word, probability in f_words_sorted:
                f_word = 'NULL' if not f_word else f_word
                print("{}:  {:0.4f}".format(f_word, probability))

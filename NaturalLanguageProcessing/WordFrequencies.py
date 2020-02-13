from collections import Counter
import re

SV_PATH = 'Data/europarl-v7.sv-en.lc.sv'
ENG_PATH = 'Data/europarl-v7.sv-en.lc.en'
TERMINATION_MARKS = ['.', '?', '!', ';']

def count_words(path):
    with open(path) as f:
        txt = f.read()
    # txt = re.sub('[^a-zåäö\']+', " ", txt)
    txt = re.sub('[^a-zåäö.?!;\']+', " ", txt)  # we keep the termination marks
    words_list = list(txt.split())
    # flat_list=[word for line in f for word in line.split()]
    counter = Counter(words_list)

    return words_list, counter


sv_list, sv_counter = count_words(SV_PATH)
eng_list, eng_counter = count_words(ENG_PATH)

# print(sv_counter.most_common(10))
# print(eng_counter.most_common(10))
#
# print(eng_counter['speaker']/len(eng_list))
# print(eng_counter['zebra']/len(eng_list))

bigram_counter = Counter()

for i in range(len(sv_list) - 1):
    word1 = sv_list[i]
    word2 = sv_list[i + 1]

    if word2 in TERMINATION_MARKS:
        continue

    if word1 in TERMINATION_MARKS:
        bigram_counter[word2] += 1
        continue

    bigram_counter[word1 + ' ' + word2] += 1

print(bigram_counter.most_common(20))

def maximum_likelihood(words, word):
    return bigram_counter[words]/eng_counter[word]

def probability_of(sentence):
    total_probability=bigram_counter[sentence[0]]/sv_counter[sentence[0]]

    for i in range(len(sentence) - 1):
        word_pair = sentence[i] + ' ' + sentence[i+1]
        total_probability *= bigram_counter[word_pair]/sv_counter[sentence[i]]

    return total_probability

print(probability_of(['för', 'att', 'jag']))

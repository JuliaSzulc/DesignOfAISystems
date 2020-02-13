from collections import Counter
import re

SV_PATH = 'Data/europarl-v7.sv-en.lc.sv'
ENG_PATH = 'Data/europarl-v7.sv-en.lc.en'


with open(SV_PATH) as f:
    text = f.read()
    text = re.sub('[^a-zåäö\ \']+', " ", text)
    sv_words = list(text.split())
   # flat_list=[word for line in f for word in line.split()]

sv_counter = Counter(sv_words)
print(sv_counter.most_common(10))

with open(ENG_PATH) as f:
    text = f.read()
    text = re.sub('[^a-zåäö\ \']+', " ", text)
    eng_words = list(text.split())
   # flat_list=[word for line in f for word in line.split()]

eng_counter = Counter(eng_words)
print(eng_counter.most_common(10))

print(eng_counter['speaker']/len(eng_words))
print(eng_counter['zebra']/len(eng_words))
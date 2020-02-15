from Utils import *
from Bigram import *
from Translator import *

SV_PATH = 'Data/europarl-v7.sv-en.lc2.sv'
ENG_PATH = 'Data/europarl-v7.sv-en.lc.en'


def main():
    sv_list, sv_counter = prepare_data(SV_PATH)
    eng_list, eng_counter = prepare_data(ENG_PATH)

    # print(sv_counter.most_common(10))
    # print(eng_counter.most_common(10))
    #
    # print(eng_counter['speaker'] / len(eng_list))
    # print(eng_counter['zebra'] / len(eng_list))

    bigram = Bigram(sv_list)

    sentence = "ett direktiv som utvecklas endast för direktivens egen skull " \
               "vore inte värdigt kammaren ."
    sentence = convert_text_to_words_list(sentence)

    print(bigram.calculate_probability_of_sentence(sentence))

main()

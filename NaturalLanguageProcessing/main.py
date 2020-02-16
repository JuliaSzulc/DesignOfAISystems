from Utils import *
from Bigram import *
from Translator import *

SV_PATH = 'Data/europarl-v7.sv-en.lc.sv'
ENG_PATH = 'Data/europarl-v7.sv-en.lc.en'


def main():
    sv_list = prepare_data(SV_PATH)
    eng_list = prepare_data(ENG_PATH)

    # print(sv_counter.most_common(10))
    # print(eng_counter.most_common(10))
    #
    # print(eng_counter['speaker'] / len(eng_list))
    # print(eng_counter['zebra'] / len(eng_list))

    # sv_bigram = Bigram(sv_list)
    #
    # sentence = "ett direktiv som utvecklas endast för direktivens egen " \
    #            "skull vore inte värdigt kammaren ."
    # sentence = convert_text_to_words_list(sentence)
    #
    # print(sv_bigram.calculate_probability_of_sentence(sentence))

    a = prepare_data('Data/1')
    b = prepare_data('Data/2')

    t = Translator(foreign_sentences=a,
                   native_sentences=b)
    t.train(epochs=10, printed_results=3)

main()

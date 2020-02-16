from Utils import *
from LanguageModel import *
from TranslationModel import *

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

    # sv_bigram = LanguageModel(sv_list)
    #
    # sentence = "ett direktiv som utvecklas endast för direktivens egen " \
    #            "skull vore inte värdigt kammaren ."
    # sentence = convert_text_to_words_list(sentence)
    #
    # print(sv_bigram.calculate_probability_of_sentence(sentence))

    a = prepare_data('Data/3')
    b = prepare_data('Data/4')

    t = TranslationModel(foreign_sentences=sv_list,
                         native_sentences=eng_list)
    t.train(epochs=10, printed_results=10, printed_words=['european'])

main()

from Utils import prepare_data


SV_PATH = 'Data/europarl-v7.sv-en.lc.sv'
ENG_PATH = 'Data/europarl-v7.sv-en.lc.en'
NUMBER_OF_ITERATIONS = 10



def main():
        sv_words,_ = prepare_data(SV_PATH)
        eng_words, _ = prepare_data(ENG_PATH)
        algorithm(sv_words, eng_words)


def algorithm(source_words, target_words):
    parameters = []
    for t in range(NUMBER_OF_ITERATIONS):
        C_s_e = {}
        C_e = {}




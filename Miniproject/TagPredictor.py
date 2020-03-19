import pickle


def predict_tags(model_file, question, tags_n=5):
    with open(model_file, 'rb') as f:
        model = pickle.load(f)

    tags_probabilities = model.predict([question])[0]
    tags = model.evaluate_top_n_tags(tags_n, tags_probabilities)

    return tags


if __name__ == '__main__':
    question = input('Insert a question:\n')
    predicted_tags = predict_tags('model.pkl', question)
    print('Suitable tags: {}'.format(predicted_tags))

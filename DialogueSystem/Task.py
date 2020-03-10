import re

class Task:
    def __init__(self, id, data):
        self.id = id
        self.keywords = data['keywords']
        self.form_fields = data['form_fields']
        self.rules = data['rules']
        self.response = data['response']

    def is_this_task(self, sentence):
        sentence = re.sub('[^A-Za-z0-9\s]+', '', sentence)
        sentence = sentence.split()
        return any(keyword in sentence for keyword in self.keywords)

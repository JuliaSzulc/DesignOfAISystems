class Task:

    def __init__(self, keywords, form_fields, rules):
        self.keywords = keywords

        self.form_fields = form_fields

        self.rules = rules

    def is_this_task(self, sentence):
        sentence = sentence.split()
        return any(keyword in sentence for keyword in self.keywords)

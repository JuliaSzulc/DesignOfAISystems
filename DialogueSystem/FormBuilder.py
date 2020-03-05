import re

class FormBuilder:

    def create_form(self, task, user_input, form = None):
        more_info = []
        if not form:
            form = dict.fromkeys(task.form_fields.keys())

        input_list = user_input.split()
        for regex, field in zip(task.rules, task.form_fields.keys()):
            word = re.search(regex, input_list)
            if not word:
                more_info.append(field)
            form[field] = word

        return form, more_info

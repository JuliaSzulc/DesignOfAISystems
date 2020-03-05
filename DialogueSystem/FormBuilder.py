import re

class FormBuilder:

    def create_form(self, task, user_input, form = None):
        more_info = []
        if not form:
            form = dict.fromkeys(task.form_fields)

        for regex, field in zip(task.rules, task.form_fields):
            word = re.search(regex, user_input)
            if not word:
                more_info.append(field)
            else:
                form[field] = word.group()

        return form, more_info

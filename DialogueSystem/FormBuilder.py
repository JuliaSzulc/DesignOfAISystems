import re

class FormBuilder:
    def create_form(self, task, user_input, form=None, field=None):
        more_info = []
        if form:
            form[field] = user_input
            return form, more_info

        form = dict.fromkeys(task.form_fields)
        form['id'] = int(task.id)

        for regex, field in zip(task.rules, task.form_fields):
            word = re.search(regex, user_input)
            if not word:
                more_info.append(field)
            else:
                form[field] = word.group()

        return form, more_info

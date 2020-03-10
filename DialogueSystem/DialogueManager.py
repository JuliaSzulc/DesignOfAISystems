from DialogueSystem.FormBuilder import FormBuilder


class DialogueManager:
    def __init__(self, tasks, task_manager):
        self.tasks = tasks
        self.form_builder = FormBuilder()
        self.task_manager = task_manager

    def say(self, text):
        print('\033[1m\033[92m' + text + '\033[0m')

    def talk(self):
        self.say("Hi, I am your digital Västtrafik assistant, Jessie.")
        while True:
            self.say("How can I help you today?")
            user_input = input()
            user_input = user_input.lower()
            task = self.determine_task(user_input)

            if task:
                if task.id == "BYE":
                    self.say("Have a nice day, goodbye!")
                    return
                form = self.process_input(task, user_input)
                output = self.task_manager.create_query(form)
                self.format_output(task, output)

    def process_input(self, task, user_input):
        form, more_info = self.form_builder.create_form(task, user_input)

        while more_info:
            missing_field = more_info[0]
            self.say("Please specify your {}.".format(missing_field))
            user_input = input()
            form, _ = self.form_builder.create_form(task, user_input,
                                                    form, missing_field)
            more_info.remove(missing_field)

        return form

    def determine_task(self, user_input):
        for task in self.tasks:
            if task.is_this_task(user_input):
                return task

        self.say("Sorry, I cannot understand you. Please rephrase.")
        return None

    def format_output(self, task, output):
        if not output:
            self.say("Sorry, I could not find anything.")
            return

        response = task.response

        if isinstance(output, dict):
            for partial in output.values():
                self.format_output(task, partial)
            return

        formatted = response.format(output[0], output[1], output[2], output[3],
                                    output[4], output[5])

        self.say(formatted)

from FormBuilder import *
from Task import *
from TaskManager import *


class DialogueManager:

    def __init__(self, tasks):
        self.tasks = tasks
        self.form_builder = FormBuilder()
        self.task_manager = TaskManager()

    def talk(self):
        print("Hi, I am your digital Västtrafik assistant, Jessie.")
        while True:
            user_input = input("How can I help you today?\n")
            user_input = user_input.lower()
            task = self.determine_task(user_input)

            if task:
                form = self.process_input(task, user_input)
                output = self.task_manager.get_output(form)
                print(output)


    def process_input(self, task, user_input):
        form, more_info = self.form_builder.create_form(task, user_input)

        while more_info:
            missing_field = more_info[0]
            user_input = input("Please specify your {}.\n".format(missing_field))
            form, _ = self.form_builder.create_form(task, user_input, form)
            more_info.remove(missing_field)

        return form


    def determine_task(self, user_input):
        for task in self.tasks:
            if task.is_this_task(user_input):
                return task

        print("Sorry, I cannot understand you. Please rephrase.\n")
        return None




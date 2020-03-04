from FormBuilder import *
from Task import *


class DialogueManager:

    def __init__(self, task_file_name):
        self.tasks = task_file_name
        self.form_builder = FormBuilder()

    def initialize_conversation(self):
        while True:
            user_input = input("Hi, I am your digital Västtrafik assistant Vivvi, what can I help you with?\n")
            task = self.determine_task(user_input)

            if task:
                form_builder.create_form(task, user_input)


        #Process

    def determine_task(self, user_input):
        for task in self.tasks:
            if task.is_this_task(user_input):
                return task

        print("Sorry, I cannot understand you. Please rephrase.\n")
        return None
        #Cannot be determined -> initialize conversation again
        #task -> fill a form for that task



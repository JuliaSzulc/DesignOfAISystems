import json

from DialogueSystem.Task import Task
from DialogueSystem.TaskManager import TaskManager
from DialogueSystem.DialogueManager import DialogueManager

class DialogueAgent:
    def __init__(self, credentials, filename='task_data.json'):
        self.tasks = []
        self.prepare_tasks(filename)

        self.tm = TaskManager(credentials)
        self.dm = DialogueManager(self.tasks, self.tm)

    def prepare_tasks(self, filename):
        with open(filename) as file:
            data = json.loads(file.read())
        for id, data in data.items():
            self.tasks.append(Task(id, data))

    def run(self):
        self.dm.talk()
from DialogueManager import *
from Task import *

import json


def prepare_tasks(filename='task_data.json'):
    with open(filename) as file:
        data = json.loads(file.read())
    tasks = []
    for _,value in data.items():
        tasks.append(Task(value["keywords"], value["form_fields"], value["rules"]))
    return tasks


if __name__ == '__main__':
    dm = DialogueManager(prepare_tasks())
    dm.talk()

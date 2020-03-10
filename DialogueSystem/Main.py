from DialogueSystem.DialogueAgent import DialogueAgent


if __name__ == '__main__':
    credentials = {
        'key': 'NPh8uEryvOnMabfZmdnh16c7xwMa',
        'secret': 'Tg8gKHnK0h1hog1odVIEZ46W1XAa'}

    agent = DialogueAgent(credentials)
    agent.run()

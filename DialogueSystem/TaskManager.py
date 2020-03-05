
class TaskManager:

    def create_query(self, form):
        return {'time': '12:30', 'line': '5'}

    def get_output(self, form):
        return self.create_query(form)

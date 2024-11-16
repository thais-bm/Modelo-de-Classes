# This is based off a basic CRUD (Crate-Read-Update-Delete) model
class Disciplines:

    # Creates a Discipline Object
    def __init__(self, name, code, workload, teacher=None):
        self.name = name
        self.code = code
        self.workload = workload
        self.teacher = teacher
        print(f'A disciplina {self.name} ID: {self.code} foi criada.')

    # Outputs the information of the discipline
    def get_info(self):
        info = {
            'Nome da matéria: ': self.name,
            'Código da matéria: ': self.code,
            'Carga Horária: ': self.workload,
            'Professores: ': self.teacher if self.teacher else 'Nenhum professor atribuído'
        }
        for key, value in info.items():
            print(f'{key}{value}')

    # Adds a Teacher to discipline
    def add_teacher(self):
        pass

    # Deletes a Teacher to discipline
    def delete_teacher(self):
        pass

    # Changes information of a discipline
    def update(self, name, code, workload, teacher=None):
        self.name = name
        self.code = code
        self.workload = workload
        self.teacher = teacher
        print(f'A disciplina {self.name} ID: {self.code} foi atualizada.')

    # Erases a discipline
    def __del__(self):
        print(f'A disciplina {self.name} ID: {self.code} foi deletada.')

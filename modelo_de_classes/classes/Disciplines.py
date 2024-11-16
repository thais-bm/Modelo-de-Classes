
class Disciplines:

    def __init__(self, name, code, workload, teacher=None):
        self.name = name
        self.code = code
        self.workload = workload
        self.teacher = teacher
        print(f'A disciplina {self.name} ID: {self.code} foi criada.')

    def get_info(self):
        info = {
            'Nome da matéria: ': self.name,
            'Código da matéria: ': self.code,
            'Carga Horária: ': self.workload,
            'Professores: ': self.teacher
        }
        for key, value in info.items():
            print(f'{key}{value}')

    def update(self, name, code, workload, teacher=None):
        self.name = name
        self.code = code
        self.workload = workload
        self.teacher = teacher
        print(f'A disciplina {self.name} ID: {self.code} foi atualizada.')

    def __del__(self):
        print(f'A disciplina {self.name} ID: {self.code} foi deletada.')

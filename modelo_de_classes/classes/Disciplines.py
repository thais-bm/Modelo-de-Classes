# This is based off a basic CRUD (Crate-Read-Update-Delete) model
class Disciplines:

    # Creates a Discipline Object
    def __init__(self, name, code, workload):
        self.name = name
        self.code = code
        self.workload = workload
        self.professors = []
        print(f'A disciplina {self.name} ID: {self.code} foi criada.')

    # Outputs the information of the discipline
    def get_info(self):
        info = {
            'Nome da matéria: ': self.name,
            'Código da matéria: ': self.code,
            'Carga Horária: ': self.workload,
        }
        for key, value in info.items():
            print(f'{key}{value}')

        if not self.professors == []:
            print(f'professores:')
            for professor in self.professors:
                print(f'\n  {professor.name} ID: {professor.ID}\n')
        else:
            print(f'Nenhum professor atribuído.\n')

    # Adds a Teacher to discipline
    def add_professor(self, professor):
        if not professor in self.professors:
            self.professors.append(professor)
            print(f"Professor adicionado a {self.name}.\n")
        else:
            print(f"Professor já ministra {self.name}.\n")

    # Deletes a Teacher to discipline
    def delete_professor(self, professor):
        if professor in self.professors:
            self.professors.remove(professor)
            print(f'{professor.name} removido(a) de {self.name}')
        else:
            print(f'Professor não ministra {self.name}.\n')

    # Changes information of a discipline
    def update(self, name, code, workload, professor=None):
        self.name = name
        self.code = code
        self.workload = workload
        self.professor = professor
        print(f'A disciplina {self.name} ID: {self.code} foi atualizada.')

    # Erases a discipline
    def __del__(self):
        print(f'A disciplina {self.name} ID: {self.code} foi deletada.')
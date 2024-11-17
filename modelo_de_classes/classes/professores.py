# This is based off a basic CRUD (Crate-Read-Update-Delete) model
class Professor:

    # Creates a teacher Object
    def __init__(self, name, code, departament):
        self.name = name
        self.ID = code
        self.departament = departament
        self.disciplines = []
        print(f'O professor {self.name} ID: {self.ID} foi adicionado.')

    # Outputs the information of the teacher
    def get_info(self):
        info = {
            'Nome: ': self.name,
            'ID: ': self.ID,
            'Departamento: ': self.departament,
            'Disciplinas: ': self.disciplines if self.disciplines else 'Nenhuma disciplina atribuída'
        }
        for key, value in info.items():
            print(f'{key}{value}')

    # Adds a discipline to Teacher
    def add_discipline(self, subject):
        self.disciplines.append(subject)

    # Deletes a discipline to Teacher
    def delete_teacher(self, subject):
        self.disciplines.remove(subject)

    # Changes information of a teacher
    def update(self, name, code, departament, disciplines=None):
        self.name = name
        self.ID = code
        self.departament = departament
        self.disciplines = disciplines
        print(f'As informações do professor {self.name} ID: {self.ID} foram atualizadas.')

    # Erases a teacher
    def __del__(self):
        print(f'As informações do professor {self.name} ID: {self.ID} foram deletadas.')
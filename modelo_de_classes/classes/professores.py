# This is based off a basic CRUD (Crate-Read-Update-Delete) model
# Professores.py

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
            'Departamento: ': self.departament.name,
            'Departamento da Universidade: ': self.departament.university.university_name,
            'Disciplinas: ': [f'{disciplines.name} ID: {disciplines.code}' for disciplines in self.disciplines]
                                if self.disciplines else 'Nenhuma disciplina atribuída'
        }
        for key, value in info.items():
            print(f'{key}{value}')
        print('\n')

    # Adds a discipline to Teacher
    def add_discipline(self, subject):
        self.disciplines.append(subject)

    # Deletes a discipline to Teacher
    def remove_discipline(self, subject):
        self.disciplines.remove(subject)

    # Changes information of a teacher
    def update(self, name, code, departament, disciplines=None):
        self.name = name
        self.ID = code
        self.departament = departament
        self.disciplines = disciplines
        print(f'As informações do professor {self.name} ID: {self.ID} foram atualizadas.')

    # Erases a teacher
    def delete(self):
        print(f'As informações do professor {self.name} ID: {self.ID} foram deletadas.')
        self.name = None
        self.ID = None
        self.departament = None
        self.disciplines.clear()
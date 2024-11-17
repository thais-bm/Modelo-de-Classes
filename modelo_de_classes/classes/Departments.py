# This is based off a basic CRUD (Crate-Read-Update-Delete) model
# Departments.py

class Department:
    def __init__(self, department_name, departament_code):
        self.name = department_name
        self.code = departament_code
        self.university = None
        self.professores = []
        print(f'O departamento {self.name} Código: {self.code} foi criado.')

    # Outputs the information of the department
    def get_info(self):
        info = {
            'nome: ': self.name,
            'codigo: ': self.code,
            'universidade: ': self.university.university_name,
            'professores: ': [f'{professor.name} ID: {professor.ID}' for professor in self.professores]
                            if self.professores else 'No professores assigned'
        }

        for key, value in info.items():
            print(f'{key}{value}')
        print('\n')

    # Shows the name and ID of all teachers who are in the department
    def list_teachers(self):
        print(f'Professores do departamento de {self.name}: {[f'{professor.name} ID: {professor.ID}' for professor in self.professores]
                                                            if self.professores else 'No professores assigned'}')
        print('\n')

    # Adds a teacher to the department (if he's in another department, he will warn and not add it)
    def add_teacher(self, professor):
        if professor.departament is None:
            self.professores.append(professor)
            professor.departament = self
            print(f'Professor {professor.name} adicionado ao departamento {self.name}.')
        else:
            print(f'Professor {professor.name} já está adicionado ao departamento {professor.departament.name}.')

    # Deletes a teacher from the department
    def delete_teacher(self, professor):
        self.professores.remove(professor)
        professor.departament = None
        print(f'Professor {professor.name} removido do departamento {self.name}.')

    # Updates department's information
    def update_department(self, departament_name, departament_code, departament_university, professores=None):
        self.name = departament_name
        self.code = departament_code
        self.university = departament_university
        if professores:
            self.professores = professores
        print(f'Departmento {self.name} atualizado.')

    # It changes a teacher from a department to another
    def update_professor_department(self, professor, new_department):
        old_department = professor.departament
        if old_department:
            old_department.delete_teacher(professor)
        new_department.add_teacher(professor)
        professor.departament = new_department
        if old_department:
            print(f'Professor {professor.name} movido de {old_department.name} para {new_department.name}.')
        else:
            print(f'Professor {professor.name} adicionado ao departamento {new_department.name}.')

    # Deletes a department
    def delete_department(self):
        print(f'Departamento {self.name} deletado.')
        for professor in self.professores:
            professor.departament = None
        self.professores.clear()
        self.name = None
        self.code = None
        self.university = None


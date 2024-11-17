# This is based off a basic CRUD (Crate-Read-Update-Delete) model
# Departments.py

class Department:
    def __init__(self, department_name, departament_code):
        self.name = department_name
        self.code = departament_code
        self.university = None
        self.professores = []

    # Outputs the information of the department
    def get_info(self):
        info = {
            'name': self.name,
            'code': self.code,
            'university': self.university,
            'professores': [f'{professor.name} ID: {professor.ID}' for professor in self.professores]
                            if self.professores else 'No professores assigned'
        }

        for key, value in info.items():
            print(f'{key}{value}')
        print('\n')

    # Shows the name and ID of all teachers who are in the department
    def list_teachers(self):
        info = {
            'professores: ': [f'{professor.name} ID: {professor.ID}' for professor in self.professores]
                            if self.professores else 'No professores assigned'
        }
        for key, value in info.items():
            print(f'{key}{value}')
        print('\n')

    # Adds a teacher to the department (if he's in another department, he will warn and not add it)
    def add_teacher(self, professor):
        if professor.departament is None:
            self.professores.append(professor)
            professor.departament = self
            print(f'Professor {professor.name} added to department {self.name}.')
        else:
            print(f'Professor {professor.name} already added to department {professor.departament.name}.')

    # Deletes a teacher from the department
    def delete_teacher(self, professor):
        self.professores.remove(professor)
        professor.departament = None
        print(f'Professor {professor.name} removed from department {self.name}.')

    # Updates department's information
    def update_department(self, departament_name, departament_code, departament_university, professores=None):
        self.name = departament_name
        self.code = departament_code
        self.university = departament_university
        if professores:
            self.professores = professores
        print(f'Department {self.name} updated.')

    # It changes a teacher from a department to another
    def update_professor_department(self, professor, new_department):
        old_department = professor.departament
        if old_department:
            old_department.delete_teacher(professor)
        new_department.add_teacher(professor)
        professor.departament = new_department
        if old_department:
            print(f'Professor {professor.name} moved from {old_department.name} to {new_department.name}.')
        else:
            print(f'Professor {professor.name} assigned to department {new_department.name}.')

    # Deletes a department
    def delete_department(self):
        for professor in self.professores:
            professor.departament = None
        self.professores.clear()
        self.name = None
        self.code = None
        self.university = None
        print(f'Department {self.name} deleted.')


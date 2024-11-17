
class Universidade:
    def __init__(self, university_name, university_id):
        self.university_name = university_name
        self.university_ID = university_id
        self.departments = []  # Lista de departamentos (não mais um único departamento)

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
            department.university = self
            print(f'Department {department.name} Added to {self.university_name}.')
        else:
            print(f'Department {department.name} is already added to {self.university_name}.')

    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            department.university = None
            print(f'Department {department.name} Removed from {self.university_name}.')
        else:
            print(f'Department {department.name} not found in {self.university_name}.')

    def list_departments(self):
        print(f'Departments of {self.university_name}:')
        for department in self.departments:
            print(department.name)

    def get_info(self):
        info = {
            'Nome da Universidade': self.university_name,
            'ID: ': self.university_ID,
            'Departamentos: ': [department.name for department in self.departments]
                                if self.departments else 'No Disciplines assigned'
        }
        for key, value in info.items():
            print(f'{key}{value}')
        print('\n')

    def update_department_to_university(self, department, new_university):
        old_university = department.university
        if old_university:
            old_university.remove_department(department)
        new_university.add_department(department)
        department.university = new_university
        print(f'{department.name} moved from {old_university.university_name if old_university else "None"} to {new_university.university_name}.')

    def update_universidade(self, university_name, university_id):
        self.university_name = university_name
        self.university_ID = university_id
        print(f'University updated to {self.university_name} (ID: {self.university_ID}).')

    def delete_university(self):
        print(f'{self.university_name} is being deleted...')
        for department in self.departments:
            department.delete_department()
        self.departments.clear()
        self.university_name = None
        self.university_ID = None

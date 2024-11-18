
class Universidade:
    def __init__(self, university_name, university_id):
        self.university_name = university_name
        self.university_ID = university_id
        self.departments = []
        print(f'A universidade {self.university_name} ID: {self.university_ID} foi criada.')

    def add_department(self, department):
        if department not in self.departments:
            self.departments.append(department)
            department.university = self
            print(f'Departamento {department.name} adicionado a universidade {self.university_name}.')
        else:
            print(f'Departamento {department.name} já pertence a universidade {self.university_name}.')

    def remove_department(self, department):
        if department in self.departments:
            self.departments.remove(department)
            department.university = None
            print(f'Departamento {department.name} removido de {self.university_name}.')
        else:
            print(f'Departamento {department.name} não encontrado em {self.university_name}.')

    def list_departments(self):
        print(f'Departamentos de {self.university_name}:')
        if len(self.departments) > 0:
            for department in self.departments:
                print(f'{department.name} - {department.code}\n')
        else:
            print('\n\nNenhum departamento na universidade.\n')


    def get_info(self):
        info = {
            'Nome da Universidade: ': self.university_name,
            'ID: ': self.university_ID,
            'Departamentos: ': [department.name for department in self.departments]
                                if self.departments else 'Sem departamentos designados'
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
        print(f'{department.name} movido de {old_university.university_name if old_university else "None"} para {new_university.university_name}.')

    def update_universidade(self, university_name, university_id):
        self.university_name = university_name
        self.university_ID = university_id
        print(f'Universidade atualizado para {self.university_name} (ID: {self.university_ID}).')

    def delete_university(self):
        print(f'{self.university_name} foi deletado')
        for department in self.departments:
            department.delete_department()
        self.departments.clear()
        self.university_name = None
        self.university_ID = None

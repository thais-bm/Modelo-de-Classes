# Main
from classes import universidade as uni
from classes import Departments as Depart
from classes import Disciplines as Dp
from classes import professores as pf

existing_ID_list = []


def not_ready():
    print('Não ta pronto')


def teste_disciplinas():
    pass


def id_generate(name=str()):
    new_id = str()
    word_without_preposition = str()
    id_index = 1
    preposition = [' de ', ' do ', ' dos ', ' da ', ' das ']
    for prep in preposition:
        word_without_preposition = name.lower().replace(prep, ' ').split()
    for word in word_without_preposition:
        new_id += word[0]
        if word.isnumeric() and len(new_id) > 3:
            new_id = new_id[:2] + word[0] + new_id[3:]

    while len(new_id) < 3:
        new_id += '0'
    new_id = new_id[:3]

    while (new_id + str(id_index)) in existing_ID_list:
        id_index += 1

    new_id = (new_id + str(id_index))

    existing_ID_list.append(new_id)

    return new_id


def delete_professor(prof):
    for materia in prof.disciplines:
        materia.remove_professor(prof)
    prof.delete()


def delete_discipline(materia):
    for prof in materia.professors:
        prof.disciplines.remove(materia)
    materia.delete()


def add_prof_to_class(prof, materia):
    prof.add_discipline(materia)
    materia.add_professor(prof)


def create_universities():
    print('\n== Adicionando nova universidade. ==')
    answer = str(input('Nome: '))
    new_name = answer
    new_id = id_generate(answer)

    while True:
        print(f'\n\nAdicionar universidade "{new_name} - {new_id}"?\n1 - Sim\n0 - Não\n\n')
        answer = str(input("Escolha uma opção: "))
        if answer == '1':
            universidades.append(uni.Universidade(new_name, new_id))
            break
        elif answer == '0':
            existing_ID_list.remove(new_id)
            break


def list_universities():
    if not universidades:
        print("\nNenhuma universidade registrada.")
    else:
        print('== Universidades existentes ==')
        for uni in universidades:
            print(f'{uni.university_name} - {uni.university_ID}')


def manage_universities():
    while True:
        print("\n--- Gerenciar Universidades ---")
        print('1 - Criar Universidade\n'
              '2 - Listar Universidade\n'
              '3 - Selecionar Universidades existentes\n'
              '0 - Voltar\n'
              '\n')
        answer = str(input("Escolha uma opção: "))

        # Create Uni
        if answer == '1':
            create_universities()
        # List Univ
        elif answer == '2':
            list_universities()
        # Select existing Uni
        elif answer == '3':
            access_id = str(input('\nID da universidade a ser acessada: ')).lower()
            accessed_university = None
            for universidade in universidades:
                if universidade.university_ID == access_id:
                    accessed_university = universidade
                    selected_university_menu(accessed_university)
                else:
                    accessed_university = access_id
                    print(f"Universidade de ID {accessed_university} não encontrada.")
        # Exit menu
        elif answer == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


# Adds a department to a university
def add_department_to_university(university):
    print(f"Adicionando novo departamento para {university.university_name}.")
    name = input("Nome do Departamento: ")
    code = id_generate(name)
    while True:
        print(
            f'\n\nAdicionar departamento {name} - {code} em {university.university_name} - {university.university_ID}"?'
            f'\n1 - Sim\n'
            f'0 - Não\n'
            f'\n')
        answer = str(input("Escolha uma opção: "))
        if answer == '1':
            department = Depart.Department(name, code)
            uni.Universidade.add_department(university, department)
            break
        elif answer == '0':
            existing_ID_list.remove(code)
            print("Operação cancelada.")
            break
        else:
            print("Opção inválida.")


def delete_university(university):
    while True:
        print(f'\nDeseja apagar "{university.university_name}"?')
        print("1 - Sim\n0 - Não")
        answer = str(input("Escolha uma opção: "))
        if answer == '1':
            universidades.remove(university)
            uni.Universidade.delete_university(university)
            print(f"Universidade {university.university_name} apagada com sucesso.")
            return True
        elif answer == '0':
            print("Operação cancelada.")
            return False
        else:
            print("Opção inválida.")


def update_university_info(university):
    while True:
        print(f"Atualizando dados de {university.university_name}.")
        name = input("Novo nome da Universidade: ")
        code = id_generate(name)

        # Perguntar confirmação
        print(f'\n\nConfirma mudar o nome de {university.university_name} - {university.university_ID} '
              f'para {name} - {code}?')
        print(f'1 - Sim\n0 - Não\n')
        answer = str(input("Escolha uma opção: "))

        if answer == '1':
            # Realizar atualização
            uni.Universidade.update_universidade(university, name, code)
            break
        elif answer == '0':
            print("Operação cancelada.")
            break
        else:
            print("Opção inválida. Tente novamente.")


def selected_university_menu(university):
    while True:
        print(f"\n--- Gerenciar Universidade: {university.university_name} ---")
        print("1. Listar Departamentos")
        print("2. Adicionar Departamento")
        print("3. Selecionar Departamento")
        print('4. Deletar Universidade')
        print('5. Atualizar Universidade')
        print('6. Informacoes da Universidade')
        print("0. Voltar\n")

        answer = str(input("Escolha uma opção: "))
        if answer == '0':
            break
        elif answer == '1':
            university.list_departments()
        elif answer == '2':
            add_department_to_university(university)
        elif answer == '3':
            select_to_manage_departments(university)
        elif answer == '4':
            if delete_university(university):
                return
        elif answer == '5':
            update_university_info(university)
        elif answer == '6':
            print('== Informações ==')
            uni.Universidade.get_info(university)


def list_professors(department):
    print(f'Professores do {department.name}')
    if len(department.professores) == 0:
        print('Nenhum professor encontrado.')
    else:
        for professor in department.professores:
            print(f'{professor.name} - {professor.ID}')


def add_existing_professor(department):
    print(f'\nDigite o ID do professor existente para adicionar a {department.name}:')
    professor_id = str(input())
    found_professor = None
    for professor in professores_geral:
        if professor.ID == professor_id:
            found_professor = professor
            break

    if found_professor:
        department.add_teacher(found_professor)
        print(f'Professor {found_professor.self} adicionado com sucesso ao {department.name}.')
    else:
        print('Professor não encontrado.')


def add_new_professor(department):
    print(f'Criando um novo professor para adicionar ao departamento {department.name}.')
    name = str(input("Nome do professor: "))
    new_id = id_generate(name)  # Gerar um novo ID para o professor
    new_professor = pf.Professor(name, new_id)
    department.add_teacher(new_professor)
    professores_geral.append(new_professor)  # Adiciona ao banco de dados de professores


def remove_department(department, university):
    print(f'Removendo departamento {department.name}.')
    uni.Universidade.remove_department(university, department)
    print(f'Departamento {department.name} removido com sucesso de {university.university_name}.')
    # Departamento não vive sem a universidade, então se apagar, ele morre
    Depart.Department.delete_department(department)


def add_professor(department):
    while True:
        print(f'\nAdicionando professor a {department.name}.\n'
              f'1 - Professor existente\n'
              f'2 - Professor novo\n'
              f'0 - Voltar')
        answer = str(input("Escolha uma opção: "))
        if answer == '0':
            break
        elif answer == '1':
            add_existing_professor(department)
        elif answer == '2':
            add_new_professor(department)
        else:
            print("Opção inválida.")


def select_professor(department):
    prof_exists = False
    answer = str(input('ID do professor no departamento: '))
    for professor in department.professores:
        if professor.ID == answer:
            manage_selected_professor(professor, department)
            prof_exists = True
            break
    if not prof_exists:
        print('\nProfessor não encontrado ou não existe')


def manage_department(department):
    while True:
        print(
            f'\nDEPARTAMENTO {department.name}\n'
            f'1 - Listar professores\n'
            f'2 - Selecionar professor\n'
            f'3 - Adicionar professor\n'
            f'4 - Apagar departamento\n'
            f'0 - Voltar')
        answer = str(input("Escolha uma opção: "))

        if answer == '0':
            break
        elif answer == '1':
            list_professors(department)
        elif answer == '2':
            select_professor(department)
        elif answer == '3':
            add_professor(department)
        elif answer == '4':
            remove_department(department, department.university)
            break
        else:
            print("Opção inválida.")


def select_to_manage_departments(university):
    exists = False
    if len(university.departments) == 0:
        print('\nNenhum departamento encontrado')
    else:
        answer = str(input(f'\nID do departamento a ser acessado em {university.university_name}: '))
        for dep in university.departments:
            if str(dep.code) == answer:
                exists = True
                department = dep
                manage_department(department)  # Chama a função para gerenciar o departamento
                break
        if not exists:
            print('\nDepartamento não encontrado.')


def change_add_professor_to_department(professor):
    print(f'\nAlterando departamento de {professor.name}.\nID do departamento:')
    answer = input()
    exists = False
    for dp in departments_geral:
        if dp.code == answer:
            professor.departament = dp
            exists = True
            print(f'\nDepartamento de {professor.name} alterado para {dp.name} - {dp.code}')
    if not exists:
        print(f'\nDepartamento não encontrado.')


def list_professor_disciplines(professor):
    if len(professor.disciplines) == 0:
        print('\nProfessor não leciona nenhuma disciplina.')
    else:
        for disc in professor.disciplines:
            print(f'\n{disc.name} - {disc.code} / Carga horária {disc.workload} horas')


def select_professor_discipline(professor):
    print('\nSelecionando disciplina. (nao ta pegando)\nID:')
    answer = str(input())
    exists = False
    for disc in professor.disciplines:
        if disc.code == answer:
            exists = True
            loop_disciplinas(disc)
            not_ready()
    else:
        print('\nDisciplina não lecionada pelo professor.')


def add_existing_discipline(professor):
    print('\nDisciplina existente\nID:')
    answer = str(input())
    exists_dc = False
    for dc in disciplinas_geral:
        if dc.code == answer:
            professor.add_discipline(dc)
            exists = True
    if not exists:
        print('\nDisciplina não encontrada')


def creating_discipline_to_teacher(professor):
    print(f'\nCriando disciplina e adicionando diretamente a matérias lecionadas por {professor.name}\n')
    answer = str(input('Nome da disciplina: '))
    new_name = answer
    new_id = id_generate(answer)

    print(f'\nNome: {new_name} | ID: {new_id}\nCarga Horária (em horas):')
    answer = int(input())
    new_workload = answer

    while True:
        print(f'Nova matéria criada e lecionada por {professor.name}:\n'
              f'{new_name} - {new_id} | CH: {new_workload}\n'
              f'Confirmar?\n'
              f'1 - Sim\n'
              f'0 - Não')
        answer = str(input('Escolha sua opcao: '))
        if answer == '1':
            new_discipline = Dp.Disciplines(new_name, new_id, new_workload)
            disciplinas_geral.append(new_discipline)
            professor.add_discipline(new_discipline)
            break
        else:
            existing_ID_list.remove(new_id)
            break


def manage_selected_professor(professor, department):
    while True:
        print(f'Acessando professor {professor.name} - {professor.ID}')
        if department is not None:
            print(f'departamento {professor.departament.name}')
        print(f'1 - Trocar/Adicionar a departamento\n'
              f'2 - Listar matérias lecionadas\n'
              f'3 - Selecionar matéria lecionada\n'
              f'4 - Adicionar disciplina a ser lecionada\n'
              f'0 - Voltar')
        answer = str(input('Escolha uma opção: '))
        if answer == '0':
            break
        elif answer == '1':
            change_add_professor_to_department(professor)

        elif answer == '2':
            list_professor_disciplines(professor)

        elif answer == '3':
            select_professor_discipline(professor)

        elif answer == '4':
            creating_discipline_to_teacher(professor)


def loop_disciplinas(disciplina):
    pass


def main_menu():
    while True:
        print(f'\nSISTEMA {system_name}\n'
              f'SELECIONAR OPÇÃO:\n'
              f'1 - Gerenciar Universidades\n'
              f'2 - Gerenciar Departamentos (talvez eu remova ele)\n'
              f'3 - Gerenciar Professores\n'
              f'4 - Gerenciar Disciplinas\n'
              f'0 - Finalizar\n'
              f'\n')
        answer = str(input("Escolha uma opção: "))
        if answer == '1':
            manage_universities()
        elif answer == '2':
            not_ready()
            # manage_departments()
        elif answer == '3':
            not_ready()
            # manage_professors()
        elif answer == '4':
            not_ready()
            # manage_disciplines()
        elif answer == '0':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


universidades = []
departments_geral = []
professores_geral = []
disciplinas_geral = []

system_name = 'Liceu - 100% Atualizado é Ruim de aturar'

if __name__ == "__main__":
    main_menu()

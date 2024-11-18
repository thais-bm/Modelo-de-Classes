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
    print('\nAdicionando nova universidade.\n'
         'Nome:')
    answer = str(input())
    new_name = answer
    new_id = id_generate(answer)

    while True:
        print(f'\n\nAdicionar universidade "{new_name} - {new_id}"?\n1 - Sim\n0 - Não\n\n')
        answer = str(input())
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
            print('\n\nID da universidade a ser acessada: \n')
            access_id = str(input()).lower()
            access_university = None
            for universidade in universidades:
                if universidade.university_ID == access_id:
                    access_university = universidade
                    selected_university_menu(access_university)
                else:
                    print(f"Universidade de ID {access_university} não encontrada.")
        # Exit menu
        elif answer == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")


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
        answer = str(input())
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
        answer = input().strip()
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


def selected_university_menu(university):
    while True:
        print(f"\n--- Gerenciar Universidade: {university.university_name} ---")
        print("1. Listar Departamentos")
        print("2. Adicionar Departamento")
        print("3. Selecionar Departamento")
        print('4. Deletar Universidade')
        print("0. Voltar")

        answer = str(input("Escolha uma opção: "))
        if answer == '0':
            break
        elif answer == '1':
            university.list_departments()
        elif answer == '2':
            add_department_to_university(university)
        elif answer == '3':
            # Falta Implementar
            not_ready()
            continue
        elif answer == '4':
            if delete_university(university):
                return


def main_menu():
    while True:
        print(f'\nSISTEMA {system_name}\n'
              f'SELECIONAR OPÇÃO:\n'
              f'1 - Gerenciar Universidades\n'
              f'2 - Gerenciar Departamentos\n'
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
departamentos_geral = []
professores_geral = []
disciplinas_geral = []

system_name = 'Liceu - 100% Atualizado é Ruim de aturar'

if __name__ == "__main__":
    main_menu()
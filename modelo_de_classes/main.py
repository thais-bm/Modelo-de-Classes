# Main
from classes import universidade as uni
from classes import Departments as Depart
from classes import Disciplines as Dp
from classes import professores as pf

existing_ID_list = []

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

universidades = []
departamentos_geral = []
professores_geral = []
disciplinas_geral = []

nome_do_sistema = 'nome do sistema a ser decidido'

# MAIN LOOP
while True:

    print(f'\nSISTEMA {nome_do_sistema}\nSELECIONAR OPÇÃO:\n1 - Universidades\n2 - Departamentos\n3 - Professores\n4 - Disciplinas\n0 - Finalizar\n\n')
    answer = input()
    if answer == '0':
        break
    elif answer == '1':

        # LOOP 1 - UNIVERSIDADES
        while True:
            print('\nUNIVERSIDADES\n1 - Listar\n2 - Selecionar\n3 - Adicionar\n0 - Voltar\n\n')
            answer = input()

            # 1 - Listar
            if answer == '1':
                if len(universidades) == 0:
                    print('\nNenhuma universidade registrada.')
                else:
                    for universidade in universidades:
                        print(f'\n{universidade.university_name} - {universidade.university_ID}')
            
            # 2 - Selecionar
            elif answer == '2':
                print('\n\nID da universidade a ser acessada:\n')
                access_id = input().lower()
                access_uni = 0
                exists = False
                for universidade in universidades:
                    if universidade.university_ID == access_id:
                        access_uni = universidade
                        exists = True
                # SUB-LOOP UNIVERSIDADE SELECIONADA
                if exists == True:
                    while True:
                        print(f'\nUniversidade {access_uni.university_name} - {access_id} selecionada. Selecionar opção:\n1 - Listar departamentos\n2 - Adicionar departamento\n3 - Selecionar departamento\n0 - Voltar\n\n')
                        answer = input()
                        # 0 - Voltar
                        if answer == '0':
                            break
                        # 1 - Listar departamentos
                        elif answer == '1':
                            if len(access_uni.departments) > 0:
                                for department in access_uni.departments:
                                    print(f'\n{department.name} - {department.code}')
                            else:
                                print('\nNenhum departamento encontrado.')
                        # 2 - Adicionar departamento
                        elif answer == '2':
                            print(f'\nAdicionando novo departamento para {access_uni.university_name}.\nNome:')
                            answer = input()
                            new_name = answer
                            new_id = id_generate(answer)

                            while True:
                                print(f'\n\nAdicionar departamento "{new_name} - {new_id} em {access_uni.university_name} - {access_id}"?\n1 - Sim\n0 - Não\n\n')
                                answer = input()

                                if answer == '1':
                                    access_uni.departments.append(Depart.Department(new_name, new_id))
                                    break
                                elif answer == '0':
                                    existing_ID_list.remove(new_id)
                                    break

                        # 3 - Selecionar departamento
                        elif answer == '3':
                            print('\nNão implementado :( mas não vai demorar')
                else:
                    print(f'Universidade de ID {access_id} não encontrada.')

            # 3 - Adicionar
            elif answer == '3':
                print('\nAdicionando nova universidade.\nNome:')
                answer = input()
                new_name = answer
                new_id = id_generate(answer)

                while True:
                    print(f'\n\nAdicionar universidade "{new_name} - {new_id}"?\n1 - Sim\n0 - Não\n\n')
                    answer = input()

                    if answer == '1':
                        universidades.append(uni.Universidade(new_name, new_id))
                        break
                    elif answer == '0':
                        existing_ID_list.remove(new_id)
                        break

            # 0 - Voltar
            elif answer == '0':
                break
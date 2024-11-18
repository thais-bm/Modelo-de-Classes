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

def loop_professor(professor = pf.Professor):
    while True:
        print(f'Acessando professor {professor.name} - {professor.ID}')
        if professor.departament != None:
            print(f'departamento {professor.department}')
        print(f'1 - Trocar/Adicionar a departamento\n2 - Listar matérias lecionadas\n3 - Selecionar matéria lecionada\n4 - Adicionar disciplina a ser lecionada\n0 - Voltar')
        answer = input()
        if answer == '0':
            break
        elif answer == '1':
            print(f'\nAlterando departamento de {professor.name}.\nID do departamento:')
            answer = input()
            exists = False
            for dp in departamentos_geral:
                if dp.code == answer:
                    professor.department = dp
                    exists = True
                    print(f'\nDepartamento de {professor.name} alterado para {dp.name} - {dp.code}')
            if exists == False:
                print(f'\nDepartamento não encontrado.')
        elif answer == '2':
            if len(professor.disciplines) == 0:
                print('\nProfessor não leciona nenhuma disciplina.')
            else:
                for disc in professor.disciplines:
                    print(f'\n{disc.name} - {disc.code} / Carga horária {disc.workload} horas')
        
        elif answer == '3':
            print('\nSelecionando disciplina.\nID:')
            answer = input()
            exists = False
            for disc in professor.disciplines:
                if disc.code == answer:
                    exists = True
                    loop_disciplinas(disc)
            else:
                print('\nDisciplina não lecionada pelo professor.')

        elif answer == '4':
            while True:
                print('\nAdicionando disciplina ao professor.\n1 - Disciplina existente\n2 - Disciplina nova\n0 - Voltar')
                answer = input()
                if answer == '0':
                    break
                elif answer == '1':
                    print('\nDisciplina existente\nID:')
                    answer = input()
                    exists = False
                    for dc in disciplinas_geral:
                        if dc.code == answer:
                            professor.add_discipline(dc)
                            exists == True
                    if exists == False:
                        print('\nDisciplina não encontrada')
                elif answer == '2':
                    print(f'\nCriando disciplina e adicionando diretamente a matérias lecionadas por {professor.name}\nNome da disciplina:')
                    answer == input()
                    new_name = answer
                    new_id = id_generate(answer)

                    print(f'\nNome: {new_name} | ID: {new_id}\nCarga Horária (em horas):')
                    answer = int(input)
                    new_workload = answer

                    while True:
                        print(f'Nova matéria criada e lecionada por {professor.name}:\n{new_name} - {new_id} | CH: {new_workload}\nConfirmar?\n1 - Sim\n0 - Não')
                        answer = input()
                        if answer == '1':
                            new_discipline = Dp.Disciplines(new_name, new_id, new_workload)
                            disciplinas_geral.append(new_discipline)
                            professor.add_discipline(new_discipline)
                            break
                        else:
                            existing_ID_list.remove(new_id)
                            break

def loop_disciplinas(disciplina = Dp.Disciplines):
    while True:
        print(f'Disciplina {disciplina.name} selecionada.\n1 - Listar professores que lecionam\n2 - Remover professor que leciona\n3 - Remover disciplina do sistema\n0 - Voltar')
        answer = input()
        if answer == '0':
            break
        elif answer == '1':
            for prof in disciplina.professors:
                print(f'\n{professor.name} - {professor.ID}')
        elif answer == '2':
            print('\nID do professor a ser removido:')
            answer = input
            exists = False
            for prof in disciplina.professors:
                if prof.ID == answer:
                    prof.remove_discipline(disciplina)
                    disciplina.remove_professor(prof)
                    exists == True
                    pass
            if exists == False:
                print('\nProfessor não encontrado lecionando essa disciplina.')
        elif answer == '3':
            while True:
                print(f'Tem certeza que quer remover {disciplina.name} - {disciplina.code} do sistema?\n1 - Sim\n0 - Não, voltar')
                answer = input()
                if answer == '0':
                    break
                elif answer == '1':
                    delete_discipline(disciplina)

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
                                    new_dp = Depart.Department(new_name, new_id)
                                    access_uni.departments.append(new_dp)
                                    access_uni.add_department(new_dp)
                                    break
                                elif answer == '0':
                                    existing_ID_list.remove(new_id)
                                    break

                        # 3 - Selecionar departamento
                        elif answer == '3':
                            exists = False
                            if len(access_uni.departments) == 0:
                                print('\nNenhum departamento encontrado')
                            else:
                                print(f'\nID do departamento a ser acessado em {access_uni.university_name}:')
                                answer = input()
                                for dep in access_uni.departments:
                                    if dep.code == answer:
                                        exists = True
                                        departamento = dep
                                        # SUB-LOOP DEPARTAMENTO
                                        while True:
                                            print(f'\nDEPARTAMENTO {departamento.name}\n1 - Listar professores\n2 - Selecionar professor\n3 - Adicionar professor\n4 - Remover departamento\n0 - voltar')
                                            answer = input()

                                            # 0 - Voltar
                                            if answer == '0':
                                                break

                                            # 1 - Listar professores
                                            elif answer == '1':
                                                if len(departamento.professores) == 0:
                                                    print('Nenhum professor encontrado.')
                                                else:
                                                    for professor in departamento.professores:
                                                        print(f'\n{professor.self} - {professor.ID}')
                                            
                                            # 2 - Selecionar professor
                                            elif answer == '2':
                                                prof_exists = False
                                                print('ID do professor no departamento')
                                                for professor in departamento:
                                                    if professor.ID == answer:
                                                        loop_professor(professor)
                                                        prof_exists = True
                                                if not prof_exists:
                                                    print('\nProfessor não encontrado ou não existe')

                                            # 3 - Adicionar professor
                                            elif answer == '3':
                                                while True:
                                                    print(f'\nAdicionando professor a {departamento.name}.\n1 - Professor existente\n2 - Professor novo\n 0 - Voltar')
                                                    answer = input()

                                                    # 0 - Voltar
                                                    if answer == '0':
                                                        break
                                                    
                                                    # 1 - Professor existente
                                                    elif answer == '1':
                                                        if len(professores_geral) == 0:
                                                            print('\nNenhum professor registrado no sistema.')
                                                        else:
                                                            print(f'\nAdicionando professor ao departamento {departamento.name}.\nID:')
                                                            answer == input()
                                                            for prof in professores_geral:
                                                                if prof.ID == answer:
                                                                    departamento.add_teacher(prof)
                                                    
                                                    # 2 - Professor novo
                                                    elif answer == '2':
                                                        print('\nAdicionando novo professor diretamente ao departamento.\nNome:')
                                                        answer = input()
                                                        new_name = answer
                                                        new_id = id_generate(new_name)

                                                        while True:
                                                            print(f'Adicionar {new_name} - {new_id} ao sistema e diretamente ao departamento {departamento.name}?\n1 - Sim\n0 - Não')
                                                            answer = input()
                                                            if answer == '0':
                                                                existing_ID_list.remove(new_id)
                                                                break
                                                            elif answer == '1':
                                                                new_prof = pf.Professor(new_name, new_id, departamento)
                                                                departamento.professores.append(new_prof)
                                                                professores_geral.append(new_prof)
                                                                break
                                if exists == False:
                                    print('\nProfessor não encontrado.')
                                
                        # 4 - Remover departamento
                        elif answer == '4':
                            while True:
                                print(f'Tem certeza que deseja remover o departamento {departamento.name}?\n1 - Sim\n0 - Não, voltar.')
                                answer = input()
                                if answer == 0:
                                    break
                                elif answer == 1:
                                    departamento.delete_department()
                                    break                   
                                                
                                            

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
        
        # LOOP 2 - Departamentos
    elif answer == '2':
        while True:
            print(f'DEPARTAMENTOS\n1 - Listar\n2 - Adicionar novo\n3- Selecionar\n0 - Voltar')
            answer = input()
            if answer == '1':
                if len(departamentos_geral) == 0:
                    print('Nenhum departamento registrado')
                else:
                    for dp in departamentos_geral:
                        print(f'\n{dp.name} - {dp.code}')
                        if dp.university != None:
                            print(f'{dp.university}')
            
            elif answer == '2':
                if len(universidades) == 0:
                    print('Departamentos não podem ser criados sem que exista uma universidade.')
                else:
                    print('Criando departamento.\nID da universidade onde o departamento será criado:')
                    answer = input()
                    univ = None
                    exists = False
                    for univeridade in universidades:
                        if univeridade.university_id == answer:
                            univ = univeridade
                            exists = True
                    if exists == False:
                        print('\nUniversidade não encontrada.')
                    else:
                        print('\nNome do departamento novo:')
                        answer = input()
                        new_name = answer
                        new_id = id_generate(new_name)

                        while True:
                            print(f'Criar departamento {new_name} - {new_id} em {univ.name}?\n1 - Sim\n0 - Não')
                            answer = input()

                            if answer == '0':
                                existing_ID_list.remove(new_id)
                                break
                            elif answer == '1':
                                new_dp = Depart.Department(new_name, new_id)
                                univ.add_department(new_dp)
                                departamentos_geral.append(new_dp)
            elif answer == '3':
                #colocar aqui a função com o loop de quando seleciona um departamento pelo menu da universidade
                pass

            elif answer == '0':
                break

    # loop 3 professores :(
    elif answer == '3':
        while True:
            print('Professores\n1 - Listar\n2 - Adicionar\n3 - Selecionar\n0 - Voltar')
            answer = input()
            if answer == '0':
                break
            elif answer == '1':
                if len(professores_geral) == 0:
                    print('\nnenhum professor registrada')
                else:
                    for disc in professores_geral:
                        print(f'\n{disc.name} - {disc.ID}')

            elif answer == '2':
                print('\nAdicionando nova disciplina.\nNome:')
                answer = input()
                new_name = answer
                new_id = id_generate(answer)

                while True:
                    print(f'\n\nAdicionar professor {new_name} - {new_id}?\n1 - Sim\n0 - Não\n\n')
                    answer = input()

                    if answer == '1':
                        new_disc = pf.Professor(new_name, new_id)
                        professores_geral.append(new_disc)
                        break
                    elif answer == '0':
                        existing_ID_list.remove(new_id)
                        break
            
            elif answer == '3':
                print('\nSelecionando professor existente.\nID:')
                answer = input()
                exists = False
                for disc in professores_geral:
                    if disc.ID == answer:
                        loop_professor(disc)
                        pass
            
            

    #4 loop das disciplinas nao aguento mais
    elif answer == '4':
        while True:
            print('\nDisciplinas\n1 - Listar\n2 - Criar nova\n3 - Selecionar\n0 - Voltar')
            answer = input()
            if answer == '0':
                break
            elif answer == '1':
                if len(disciplinas_geral) == 0:
                    print('\nnenhuma disciplina registrada')
                else:
                    for disc in disciplinas_geral:
                        print(f'\n{disc.name} - {disc.code} | carga horária :{disc.workload}')
            
            elif answer == '2':
                print('\nAdicionando nova disciplina.\nNome:')
                answer = input()
                new_name = answer
                new_id = id_generate(answer)

                print('\nCarga horária:')
                answer = int(input())
                new_workload = answer

                while True:
                    print(f'\n\nAdicionar disciplina {new_name} - {new_id} com carga horária de {new_workload}h?\n1 - Sim\n0 - Não\n\n')
                    answer = input()

                    if answer == '1':
                        new_disc = Dp.Disciplines(new_name, new_id,new_workload)
                        disciplinas_geral.append(new_disc)
                        break
                    elif answer == '0':
                        existing_ID_list.remove(new_id)
                        break
            elif answer == '3':
                print('\nSelecionando disciplina existente.\nID:')
                answer = input()
                exists = False
                for disc in disciplinas_geral:
                    if disc.code == answer:
                        loop_disciplinas(disc)
                        pass
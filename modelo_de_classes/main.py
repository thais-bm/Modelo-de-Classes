# Main
from classes import universidade as uni
from classes import Departments as Depart
from classes import Disciplines as Dp
from classes import professores as pf

existing_ID_list = []


def teste_disciplinas():
    print('Criando Professores')
    professor1 = pf.Professor('Jumento', id_generate('Jumento'), None)
    professor2 = pf.Professor('Burrico', id_generate('Burrico'), None)
    professor3 = pf.Professor('Cavalo', id_generate('Cavalo'), None)
    professor4 = pf.Professor('Ponei', id_generate('Ponei'), None)

    print('\nCriando Disciplinas')
    materia1 = Dp.Disciplines('Geografia', id_generate('Geografia'), 12)
    materia2 = Dp.Disciplines('História', id_generate('História'), 12)
    materia3 = Dp.Disciplines('Matemática Discreta', id_generate('Matemática Discreta'), 12)
    materia4 = Dp.Disciplines('Histologia de Ondas Alternantes 3', id_generate('Histologia de Ondas Alternantes 3'), 12)

    print('\nAdicionando professores a disciplinas e vice versa')
    add_prof_to_class(professor1, materia1)
    add_prof_to_class(professor2, materia1)
    add_prof_to_class(professor3, materia1)
    add_prof_to_class(professor3, materia3)
    add_prof_to_class(professor4, materia4)
    add_prof_to_class(professor1, materia2)

    print('\nMostrnado informação das disciplinas')
    materia1.get_info()
    materia2.get_info()
    materia3.get_info()
    materia4.get_info()

    print('\nMostrando informação dos professores')
    professor1.get_info()
    professor2.get_info()
    professor3.get_info()
    professor4.get_info()

    print('\nApagando os professores')
    delete_professor(professor1)
    delete_professor(professor2)
    delete_professor(professor3)

    print('\nApagando uma materia')
    delete_discipline(materia1)

    print('\nfim de tudo')


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

def teste_depart():
    departament1 = Depart.Department('Computaria', id_generate('Computaria'), 'Cabaré')
    departament2 = Depart.Department('Eu programo com C#', id_generate('eu programo com C#'), 'Cabaré')
    professor1 = pf.Professor('Cavalo', id_generate('Cavalo'), None)
    departament1.add_teacher(professor1)

    print('\n')

    departament2.update_professor_department(professor1, departament2)

    professor1.get_info()
if __name__ == '__main__':
    teste_depart()

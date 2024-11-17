from classes import universidade as Uni
from classes import Departments as Depart
from classes import Disciplines as Dp
from classes import professores as Pf

existing_ID_list = []

def teste_disciplinas():
    professor1 = Pf.Professor('Jumento', ID_generate('Jumento'), None)
    professor2 = Pf.Professor('Burrico', ID_generate('Burrico'), None)
    professor3 = Pf.Professor('Cavalo', ID_generate('Cavalo'), None)
    professor4 = Pf.Professor('Ponei', ID_generate('Ponei'), None)

    materia1 = Dp.Disciplines('Geografia', ID_generate('Geografia'), 12)
    materia2 = Dp.Disciplines('História', ID_generate('História'), 12)
    materia3 = Dp.Disciplines('Matemática Discreta', ID_generate('Matemática Discreta'), 12)
    materia4 = Dp.Disciplines('Histologia de Ondas Alternantes 3', ID_generate('Histologia de Ondas Alternantes 3'), 12)

    prof_to_class(professor1, materia1)
    prof_to_class(professor2, materia1)
    prof_to_class(professor3, materia1)
    prof_to_class(professor3, materia1)
    prof_to_class(professor4, materia1)
    prof_to_class(professor1, materia2)
    materia1.get_info()

    prof_deletion(professor1)
    prof_deletion(professor2)


def ID_generate(name = str):
    new_id = ''
    id_index = 1
    for word in name.lower().replace(' de ', ' ').replace(' do ', ' ').replace(' dos ', ' ').replace(' das ', ' ').replace(' da ', ' ').split():
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

def prof_deletion(prof = Pf.Professor):
    for materia in prof.disciplines:
        materia.delete_professor(prof)
    prof.__del__()

def prof_to_class(prof = Pf.Professor, materia = Dp.Disciplines):
    prof.add_discipline(materia)
    materia.add_professor([prof.name, prof.ID])
    print(f'professor {prof.name} adicionado na disciplina {materia.name}')

if __name__ == '__main__':
    teste_disciplinas()
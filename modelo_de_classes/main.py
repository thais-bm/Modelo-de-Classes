from classes import universidade as Uni
from classes import Departments as Depart
from classes import professores as Pf
from classes import Disciplines as Dp


def teste_disciplinas():
    professor = Pf.Teachers('Jumento', 'JEGUE', None)


    materia = Dp.Disciplines('Geografia', '34532', 12, professor)
    materia.get_info()

    materia.update('Historia', 'ABCDE', 24, 'GIROFLEX')
    materia.get_info()


if __name__ == '__main__':
    teste_disciplinas()



from classes import universidade as Uni
from classes import departamentos as Depart
from classes import professores as Pf
from classes import Disciplines as Dp


def print_hi():
    materia = Dp.Disciplines('Geografia', '34532', 12)
    materia.get_info()

    materia.update('Historia', 'ABCDE', 24, 'GIROFLEX')
    materia.get_info()


if __name__ == '__main__':
    print_hi()



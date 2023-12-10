from multiprocessing import Process

from RadicalEmpiricism.src.scripts.populate_translations import populate_translations
from RadicalEmpiricism.src.scripts.populate_definitions import populate_definitions
from RadicalEmpiricism.src.scripts.populate_etymologies import populate_etymologies

DO_TRANSLATION = False


def populate_updates():
    if DO_TRANSLATION:
        populate_translations()
    p1 = Process(target=populate_definitions)
    p2 = Process(target=populate_etymologies)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    populate_updates()

from multiprocessing import Process

from .populate_translations import populate_translations
from .populate_definitions import populate_definitions
from .populate_etymologies import populate_etymologies


def populate_updates():
    populate_translations()
    p1 = Process(target=populate_definitions)
    p2 = Process(target=populate_etymologies)
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    populate_updates()

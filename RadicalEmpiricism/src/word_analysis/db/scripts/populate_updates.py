from .populate_translations import populate_translations
from .populate_definitions import populate_definitions
from .populate_etymologies import populate_etymologies

def populate_updates():
    populate_translations()
    populate_definitions()
    populate_etymologies()


if __name__ == '__main__':
    populate_updates()

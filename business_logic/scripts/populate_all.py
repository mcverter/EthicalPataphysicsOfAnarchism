from populate_inserts import populate_inserts
from populate_updates import populate_updates


def populate_all():
    populate_inserts()
    populate_updates()


if __name__ == '__main__':
    populate_all()

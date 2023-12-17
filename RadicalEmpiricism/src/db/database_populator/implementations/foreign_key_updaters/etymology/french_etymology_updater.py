from RadicalEmpiricism.src.crawler_tools.crawler_tools import (
    get_dictionaire_des_francophone_etymology,
    get_cntrl_eymology)
from RadicalEmpiricism.src import constants
from RadicalEmpiricism.src.db.database_populator.foreign_key_updater import ForeignKeyUpdater
from RadicalEmpiricism.src.logger import log_and_print_error

OFFSET: int = 0


class FrenchEtymologyUpdater(ForeignKeyUpdater):
    def __init__(self):
        super().__init__(table=constants.TABLE_WORD,
                         set_column=constants.COLUMN_ETYMOLOGY,
                         where_column=constants.COLUMN_FRENCH,
                         fk_internal_column=constants.COLUMN_FRENCH_EXPLANATION,
                         offset=OFFSET)

    def get_fk_value_from_main_where_value(self, where_value):
        if where_value:
            cntrl = get_cntrl_eymology(where_value)
            ddf = get_dictionaire_des_francophone_etymology(where_value)
            print('etymologies', ddf, cntrl)
            return f'{ddf} ({cntrl})'
        log_and_print_error('undefined call arg ' + where_value)
        return None


if __name__ == '__main__':
    updater = FrenchEtymologyUpdater()
    updater.populate()
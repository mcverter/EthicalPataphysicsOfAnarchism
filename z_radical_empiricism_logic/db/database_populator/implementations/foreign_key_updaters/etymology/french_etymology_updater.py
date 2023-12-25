from z_radical_empiricism_logic.crawler_tools.crawler_tools import get_cntrl_eymology
import constants
from z_radical_empiricism_logic.db.database_populator.foreign_key_updater import ForeignKeyUpdater
from z_radical_empiricism_logic.logger.db_logger import log_and_print_error

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
            return get_cntrl_eymology(where_value)
        log_and_print_error('undefined call arg ' + where_value)
        return None


if __name__ == '__main__':
    updater = FrenchEtymologyUpdater()
    updater.populate()

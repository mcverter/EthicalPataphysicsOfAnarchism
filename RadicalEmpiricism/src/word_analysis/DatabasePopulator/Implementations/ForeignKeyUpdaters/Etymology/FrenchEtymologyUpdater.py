from RadicalEmpiricism.src.word_analysis.CrawlerTools.crawler_tools import (
    get_dictionaire_des_francophone_etymology,
    get_cntrl_eymology)
from ....ForeignKeyUpdater import ForeignKeyUpdater
from RadicalEmpiricism.src.word_analysis import constants

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
        else:
            print('break')

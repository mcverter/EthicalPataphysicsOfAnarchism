from RadicalEmpiricism.src.db.DbHandler import DbHandler

NUM_WORDS_SQL = \
    'select * from word_analysis_word;'
NUM_ENGLISH_WORD_SQL = \
    'select count(*) from word_analysis_word where english is not null'
NUM_WORDS_WITH_DEFINITION_SQL = \
    'select count(*) from word_analysis_word where definition_id is not null'
NUM_WORDS_WITH_ETYMOLOGY_SQL = \
    'select count(*) from word_analysis_word where etymology_id is not null'
NUM_ENGLISH_ETYMOLOGY_SQL = \
    'select count(*) from word_analysis_etymology where english_explanation is not null'
NUM_FRENCH_ETYMOLOGY_SQL = \
    'select count(*) from word_analysis_etymology where french_explanation is not null'
NUM_ENGLISH_DEFINITION_SQL = \
    'select count(*) from word_analysis_definition where english_explanation is not null'
NUM_FRENCH_DEFINITION_SQL = \
    'select count(*) from word_analysis_definition where french_explanation is not null'


class CheckTableStats:
    def __init__(self):
        self.db_handler = DbHandler()

    def log_table_stats(self):
        print(self.db_handler.execute_and_return_single_value(NUM_WORDS_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_ENGLISH_WORD_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_WORDS_WITH_DEFINITION_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_WORDS_WITH_ETYMOLOGY_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_ENGLISH_ETYMOLOGY_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_FRENCH_ETYMOLOGY_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_ENGLISH_DEFINITION_SQL))
        print(self.db_handler.execute_and_return_single_value(NUM_FRENCH_DEFINITION_SQL))


if __name__ == '__main__':
    CheckTableStats().log_table_stats()

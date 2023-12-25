from RadicalEmpiricism.src.z_radical_empiricism_logic.db.db import execute_and_return_single_value
from RadicalEmpiricism.src.z_radical_empiricism_logic.logger.stats_logger import log_stats_message

NUM_WORDS_SQL = \
    'select count(*) from word_analysis_word;'
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
    def log_table_stats(self):
        log_stats_message('Number of Words',
                          execute_and_return_single_value(NUM_WORDS_SQL))
        log_stats_message('Number of English Translations',
                          execute_and_return_single_value(NUM_ENGLISH_WORD_SQL))
        log_stats_message('Number Words with Definition',
                          execute_and_return_single_value(NUM_WORDS_WITH_DEFINITION_SQL))
        log_stats_message('Number Words with Etymology',
                          execute_and_return_single_value(NUM_WORDS_WITH_ETYMOLOGY_SQL))
        log_stats_message('Number English Etymologies',
                          execute_and_return_single_value(NUM_ENGLISH_ETYMOLOGY_SQL))
        log_stats_message('Number French Etymologies',
                          execute_and_return_single_value(NUM_FRENCH_ETYMOLOGY_SQL))
        log_stats_message('Number English Definition',
                          execute_and_return_single_value(NUM_ENGLISH_DEFINITION_SQL))
        log_stats_message('Number French Definition',
                          execute_and_return_single_value(NUM_FRENCH_DEFINITION_SQL))


if __name__ == '__main__':
    CheckTableStats().log_table_stats()

import math

from .all_counts_data import ALL_COUNTS
from .all_words_data import ALL_WORDS

TOTAL_TI_WORDS = 108498
TOTAL_OTB_WORDS = 80797


def all_words_with_counts():
    return [{
        "french": word,
        "ti": ALL_COUNTS[idx][0],
        "otb": ALL_COUNTS[idx][1],
        "sum": ALL_COUNTS[idx][0] + ALL_COUNTS[idx][1],
        "proportion": proportion_ti_to_otb(ALL_COUNTS[idx][0], ALL_COUNTS[idx][1])
    } for idx, word in enumerate(ALL_WORDS)]


def proportion_ti_to_otb(num_ti, num_otb):
    if num_otb == 0:
        return math.inf
    return round(((num_ti / num_otb) * (TOTAL_OTB_WORDS / TOTAL_TI_WORDS)), 5)

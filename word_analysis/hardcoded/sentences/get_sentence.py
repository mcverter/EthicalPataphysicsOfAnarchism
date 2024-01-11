from .otb_en import OTB_EN
from .otb_fr import OTB_FR
from .ti_en import TI_EN
from .ti_fr import TI_FR

book_language_map = {
    "otb": {
        "fr": OTB_FR,
        "en": OTB_EN,
    },
    "ti": {
        "fr": TI_FR,
        "en": TI_EN,
    }
}


def get_sentence(book, line):
    return {
        "en": book_language_map[book]["en"][line],
        "fr": book_language_map[book]["fr"][line],
    }


def get_sentence_span(book, start, end):
    return {
        "en": book_language_map[book]["en"][start:end],
        "fr": book_language_map[book]["fr"][start:end],
    }


def get_sentences_all(book):
    return {
        "en": book_language_map[book]["en"],
        "fr": book_language_map[book]["fr"],
    }

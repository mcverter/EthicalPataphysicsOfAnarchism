import re
from .all_words_get import ALL_WORDS

def genre_by_prefix(prefix):
    return [word for word in ALL_WORDS if word.startswith(re.sub('^PREFIX', '',prefix))]
def genre_by_suffix(suffix):
    return [word for word in ALL_WORDS if word.endswith(re.sub('^SUFFIX', '', suffix))]
    pass
def genre_by_morpheme(morpheme):
    return [word for word in ALL_WORDS if re.search(re.sub('^MORPHEME', '',morpheme))]

def all_genres_to_words(genre=''):
    if not genre:
        return ALL_CATEGORIES_TO_WORDS
    return ALL_CATEGORIES_TO_WORDS[genre]



def all_words_to_genres(word):
    word_to_category_dict = {}
    for category, words in ALL_CATEGORIES_TO_WORDS.items():
        for word in words:
            if word not in word_to_category_dict:
                word_to_category_dict[word] = []
            word_to_category_dict[word].append(category)

    if not word:
        return word_to_category_dict
    return word_to_category_dict[word]


ALL_CATEGORIES_TO_WORDS = {
    "ESPACE_TEMPS": {"ici", "maintenant"},
    "DANS": {'maison', 'dans', 'chez', 'interiorite'},
    "RELATION": {'relation'},
    "CONJONCTION": {'et'},
    "PHYSIQUE": {'force'},
    "FÉMININE": {'maison'},
    "TENIR": {
        "contente",
        "entrietiens",
        "impatient",
        "detient",
        "appartient",
        "contienne",
        "maintien",
        "obtient",
        "retient",
        "patience",
        "tiendrait",
        "tient",
        "appartenir",
        "contenir",
        "entretenir",
        "maintenir",
        "obtenir",
        "pro-tenir",
        "retenir",
        "soutenir",
        "tenir",
        "contenir",
        "contentement",
        "contenter",
    },
    "APPEARANCE": {
        "présence",
        "absence",
        "lumière",
        "obscur",
        "vision",
        "vision",
        "visage",
        "face",
        "façade",
        "surface",
        "tergiversation",
        "masque",
    },
    "GENÈSES": {
        "genèses",
        "origine",
        "mort",
        "résurrection",
        "recurrence",
        "naissance",
        "survivant",
        "surgit",
        "père",
        "mère",
        "fils",
        "frere",
        "sœur",
        "virilite",
        "féminin",
        "maternelle",
        "matière",
        "nourrit",
        "neutre",
        "genre",
        "engendrer",
        "génération",
    },
    "ORALITY": {
        "parler",
        "souffle",
        "rire",
        "baiser",
        "manger",
        "remords",
        "nourrit",
    },
    "THEATER": {
        "drame",
        "acte",
        "scene",
        "masque",
        "tragique",
        "travail",
        "œuvre",
        "dechets",
        "absurde",
        "fatal",
        "faire",
        "comique",
        "jouissance",
        "rire",
        "plaisir",
        "MacBeth",
        "Shakespeare",
    },
    "MATHÉMATIQUES": {
        "zero",
        "null",
        "une",
        "deuxieme",
        "tiers",
        "unicite",
        "universalite",
        "individualite",
        "dualite",
        "multiplicite",
        "pluralisme",
        "plus",
        "négatif",
        "positif",
        "transitivite",
        "asymétrie",
        "transcendance",
        "infini",
        "Leibniz",
        "intégration",
        "continu",
        "discontinuite",
        "nœud",
        "serie",
        "proximite",
        "prochain",
    },
    "GÉOMÉTRIE": {
        "origine",
        "point",
        "intervalle",
        "Descartes",
        "courbure",
        "parallelisme",
        "convexite",
        "concavite",
        "dimension",
        "niveau",
        "hauteur",
        "profondeur",
        "droiture",
    },
    "PHYSIQUE": {
        "substance",
        "element",
        "pese",
        "matière",
        "force",
        "gravité",
        "ondes",
    },
    "ONTOLOGIE": {
        "ontologie",
        "etre",
        "état",
        "autre",
        "essence",
    },
    "EPISTEMOLOGIE": {
        "savoir",
        "doute",
        "scepticisme",
    },
    "ETHIQUE": {
        "ethique",
        "bien",
        "bonté",
        "mal",
        "valeur",
        "devrait",
    },
    "PLATON": {
        "être",
        "essence",
        "vérité",
        "dialogue",
        "genèse",
        "forme",
        "matière",
    },
    "BERGSON": {
        "création",
        "durée",
    },
    "HEGEL": {
        "totalité",
        "état",
        "autre",
        "soi",
    },
    "HUSSERL": {
        "apparence",
        "passivité",
        "activité",
        "remplissement",
    },
    "HEIDEGGER": {
        "ontologie",
        "être",
        "essence",
        "existence",
        "outil",
    },
    "DESCARTES": {
        "idée",
        "infini",
        "scepticisme",
    },
    "LEIBNIZ": {
        "monade",
        "intégration",
    },
    "NIETZSCHE": {
        "rire",
        "au-delà",
        "recurrence",
        "naissance",
        "scepticisme",
        "absurde",
        "sorcières",
        "lascivite",
        "jouir",
        "gratuite",
        "jouissance",
    }
}

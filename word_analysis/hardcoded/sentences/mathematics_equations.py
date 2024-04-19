# WordForm__TransformationFunction
#
# INPUT: hauteur
# DEDUCE: root (haut) + "eur" Output suffix meaning
#
# SYNONYM_FUNCTION
#
# VERB_NOUN_CLASSIFICATION//WORD_FORM
#
# Inteserction in wors with two sets

# 4 morphemes
# WORD ONE        "résurrection", # re + sur + rect + tion 4 morphemes

def transformation_function(total_value, manifold, valence):
    pass


def word_value(morphemes):
    total_value = 1
    for m in morphemes:
        total_value = transformation_function(total_value, m.manifold, m.valence)
    return total_value


ENUM_HEIGHT = {"sur": 1, "rect": 1, "sub": -1}

ENUM_REPETITION = {"re": 1}
NOUN = {"ive": 1, "tion": 1, }


def lookup_morpheme():
    pass


v1 = word_value([
    "re",
    "sur",  # +1 HEIGHT
    "rect",  # +1 HEIGHT
    "tion"
])

v2 = word_value([
    "sub",  # -1 HEIGHT
    "ject",
    "ive",
])

# WORD TWO        "subjective" = # sub + ject + ive
# word position modifier -->
'''
book = 1 / number chapters 
chapterNum 0.1 * chapter;
section 0.01 * section 
subsection
line 
word


Kazi it took me a minute to find it... but on 94 the note about passive synthesis as contraction to the general.....
Asymmetrical in that it goes from past to the future in the present.

'''

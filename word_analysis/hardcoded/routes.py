from django.utils.translation import gettext as _

BRAND_ROUTE = {
    "route": "summary",
    "title": _("Project Summary"),
    "explanation": _(
        "A discussion of the Radical Empiricism Project, in which the advantages of a multidimensional tensor analysis of metaphorical manifolds is dimensionaland the errors of unidimensional assertions of rank are critiqued"
    ),
    "subitems": [
        {"route": "objective", "title": _("Objective"), "explanation": _("Objective"), },
        {"route": "method", "title": _("Methodology"), "explanation": _("Methodology")},
        {"route": "abstract", "title": _("Abstract"), "explanation": _("Abstract")},
        {"route": "motivation", "title": _("Motivation"), "explanation": _("Motivation"),
         "sub_sub_items": [
             {"route": "not_one_dimensional",
              "title": _("The perspectival manifold as a corrective to one-dimensional hierarchical analyses")},

             # has to be both structural and terminological

             {"route": "bernasconi_focus",
              "title": _("Robert Bernasconi on distorted focus")},
             {"route": "reasons_for_misreading",
              "title": _("Reasons for misreading")},
             {"route": "cryptic",
              "title": _("Levinas's cryptic verbiage")},
             {"route": "ontological_predication",
              "title": _(
                  "Ontological Predication (Insufficient Solution One): Clarify Obscurity with Simple Assertions")},
             {"route": "multiplication_complexities",
              "title": _("Multiplications of Complexities (Insufficient Solution #2)")},

             {"route": "orthodox_look_up",
              "title": _("The ortohodox tendency to look up to Levinas")},
             {"route": "cohen_elevations",
              "title": _("Richard Cohen's *Elevations* as Orthodox Submission")},
             {"route": "orthodox_truth_as_war",
              "title": _("Orthodox Truth as War")},
             {"route": "polarity_and_opposition", "title": "Polarity and Opposition"},
             {"route": "polar_not_war", "title": "Polar Not War"},
             {"route": "orthodox_battle_cry",
              "title": _("The orthodox battle cry of ressentiment")},
             {"route": "privilege",
              "title": _("The criticism of privilege")},
             {"route": "derrida_anarchy",
              "title": _("Derrida's anarchical critique of Levinas")},
         ]},
        {
            "route": "ambisexuality",
            "title": _("Ambiguity and ambisexuality"),
            "explanation": _("Ambiguity and ambisexuality"),
            "sub_sub_items": [
                {
                    "route": "home_and_position",
                    "title": _("Home and Position"),
                    "explanation": _("Home and Position"),
                },
                {
                    "route": "womb",
                    "title": _("The nourishing womb"),
                    "explanation": _("The nourishing womb"),
                },
                {
                    "route": "hostage",
                    "title": _("Host and Hostage"),
                    "explanation": _("Host and Hostage"),
                },
            ],
        },

    ],
}

NAV_ITEMS = [
    {
        "route": "genre_theory",
        "title": _("Theory of Genre Sets"),
        "explanation": _(
            "This page features many discussion: (1) An Introduction to Genre Sets, (2) An example analysis of a sentence from Totality and Infinity as a constellation of Genre Sets, (3) Genre Set Membership Rules, (4)Internal and External Relations"
        ),
        "subitems": [
            {"route": "genre_set_intro", "title": _("Introduction to Genre Sets")},
            {"route": "membership", "title": _("Group Set Membership")},
            # relations
            {
                "route": "combination",
                "title": _("Combination"),
                "sub_sub_items": [
                    {
                        "route": "repetition",
                        "title": _("Repetition of the same word in different context"),
                    },
                    {"route": "opposition", "title": _("Opposition")},
                    {"route": "intersection", "title": _("Intersection")},
                    {"route": "parallelism", "title": _("Parallelism")},
                ],
            },
            {
                "route": "constellation",
                "title": _(
                    "A Constellational Analysis of a Metaphorically Kallidescopic Sentence"
                ),
            },
        ],
    },
    {
        "route": "mots",
        "title": _("Word list"),
        "explanation": _(
            "A list of all 16000 words in both Totality and Otherwise. Links to information pages about each word, including definitions and etymologies in English and French, as well as frequencies and lines from both texts"
        ),
    },
    {
        "route": "genres",
        "title": _("List of Genre Sets"),
        "explanation": _("A list of Genre Sets."),
    },

    {
        "route": "topics",
        "title": _("The Mathematics Genre Set"),
        "explanation": _(
            "(1) Non-Euclidean Relations, (2) Other mathematical and scientific topics (3) Perspectivism"
        ),
        "subitems": [
            {"route": "mathematics", "title": _("The Mathematics Genre Sets")},
            # relations
            {"route": "tensor_transformation_patterns", "title": "Tensor Transformation Patterns"},
            {"route": "assorted_math_stuff_from_discussion", "title": "Assorted Math Stuff"},
            {
                "route": "curvature",
                "title": _("Curvature"),
                "sub_sub_items": [
                    {"route": "flat", "title": _("Flat")},
                    {"route": "two_dimensional", "title": _("Two Dimensional")},
                    {"route": "curvature", "title": _("Curvature")},
                ],
            },
            {"route": "perspectivism", "title": _("Perspectivism")},
            # these are all subroutes
            # this is a collection
            {
                "route": "two_dimensional",
                "title": _("Two-Dimensional Polar Relations and Two-by-Two Matrices"),
                "explanation": _("Two-Dimensional Polar Relations and Two-by-Two Matrices"),
                "sub_sub_items": [
                    {
                        "route": "flat",
                        "title": _("The flat space of totality"),
                        "explanation": _("The flat space of totality"),
                    },
                    {
                        "route": "three",
                        "title": _("Three-Dimensional Analysis"),
                        "explanation": _("Three-Dimensional Analysis"),
                    },
                ],
            },
            {"route": "numbers", "title": _("Numbers")},
            {
                "route": "plus_one",
                "title": _(
                    "The Good of the “Plus One”: Extension curved by the Vertical"
                ),
                "sub_sub_items": [
                    {"route": "zero", "title": _("Zero")},
                    {"route": "one", "title": _("One")},
                    {"route": "duality", "title": _("Duality")},
                    {"route": "three", "title": _("Three")},
                    {"route": "four", "title": _("Four")},
                    {"route": "alembert", "title": _("Quotations from d'Alembert")},
                    {"route": "brunschvicg", "title": _("Quotations from Léon Brunschvicg")},
                ],
            },

        ],
    },

#    {
#        "route": "topics",
#        "title": _("The Genesis Genre Set"),
#    },
    {
        "route": "technical",
        "title": _("Technical notes"),
        "explanation": _(
            "Contact information, sources, current project status and future direction"
        ),
    },
]

'''
    {
        "route": "topics",
        "title": _("Topics"),
        "explanation": _(
            "This page features many discussion: (1) An Introduction to Genre Sets, (2) An example analysis of a sentence from Totality and Infinity as a constellation of Genre Sets, (3) Genre Set Membership Rules [suffixes, prefixes, etymological roots, infinities, other morphemic roots, semantic themes], (4)Internal and External Relations [duality, combination, repetition, opposition, intersection], (5) Non-Euclidean Relations [parallelism, flat, two_dimensional, constellation, curvature ], (5) Other mathematical and scientific topics [addition, positive, negative, 0, 1, 2, 3, 4, infinity, set theory, continuity and infinitesimals, topology, Mikowski/Einstein space-time, wave and quantum theory  ] (6) Perspectivism [perversion, inversion, subversion, reversion] (7) Reading Totality and Infinity as Genesis and Otherwise than Being as Exodus"
        ),
    },
'''

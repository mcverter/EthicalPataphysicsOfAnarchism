from django.utils.translation import gettext as _


def all_routes_and_subroutes():
    subroutes = [nav["subitems"] for nav in nav_items if "subitems" in nav]
    return sum(subroutes, nav_items + [brand_route])


def get_page_title_for_route(route):
    return [
        nav["title"] for nav in all_routes_and_subroutes() if nav["route"] == route
    ][0]


def get_subitems_for_route(route):
    return [nav for nav in nav_items if nav["route"] == route][0]["subitems"]


brand_route = {
    "route": "summary",
    "title": _("Project Summary"),
    "explanation": _(
        "A discussion of the Radical Empiricism Project, in which the advantages of a multidimensional tensor analysis of metaphorical manifolds is dimensionaland the errors of unidimensional assertions of rank are critiqued"
    ),
    "subitems": [
        {
            "route": "objective",
            "title": _("Objective"),
            "explanation": _("Objective"),
        },
        {"route": "abstract", "title": _("Abstract"), "explanation": _("Abstract")},
        # these are all subroutes
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
        {
            "route": "discussion",
            "title": _("Discussion"),
            "explanation": _("Discussion"),
        },
    ],
}

nav_items = [
    {
        "route": "genre_theory",
        "title": _("Theory of Genre Sets"),
        "explanation": _(
            "This page features many discussion: (1) An Introduction to Genre Sets, (2) An example analysis of a sentence from Totality and Infinity as a constellation of Genre Sets, (3) Genre Set Membership Rules [suffixes, prefixes, etymological roots, infinities, other morphemic roots, semantic themes], (4)Internal and External Relations [duality, combination, repetition, opposition, intersection], (5) Non-Euclidean Relations [parallelism, flat, two_dimensional, constellation, curvature ], (5) Other mathematical and scientific topics [addition, positive, negative, 0, 1, 2, 3, 4, infinity, set theory, continuity and infinitesimals, topology, Mikowski/Einstein space-time, wave and quantum theory  ] (6) Perspectivism [perversion, inversion, subversion, reversion] (7) Reading Totality and Infinity as Genesis and Otherwise than Being as Exodus"
        ),
        "subitems": [
            {"route": "genre_set_intro", "title": _("Introduction to Genre Sets")},
            {"route": "membership", "title": _("Group Set Membership")},
            {
                "route": "constellation",
                "title": _(
                    "A Constellational Analysis of a Metaphorically Kallidescopic Sentence"
                ),
            },
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
                "route": "curvature",
                "title": _("Curvature"),
                "sub_sub_items": [
                    {"route": "flat", "title": _("Flat")},
                    {"route": "two_dimensional", "title": _("Two Dimensional")},
                    {"route": "curvature", "title": _("Curvature")},
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
                ],
            },
            {"route": "perspectivism", "title": _("Perspectivism")},
            {"route": "alembert", "title": _("Quotations from d'Alembert")},
            {"route": "brunschvicg", "title": _("Quotations from Léon Brunschvicg")},
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
        "route": "technical",
        "title": _("Technical notes"),
        "explanation": _(
            "Contact information, sources, current project status and future direction"
        ),
    },
]

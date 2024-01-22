from django.utils.translation import gettext as _


def all_routes_and_subroutes():
    subroutes = [nav["subitems"] for nav in nav_items if "subitems" in nav]
    return sum(subroutes, nav_items)


def get_page_title_for_route(route):
    return [nav["title"] for nav in all_routes_and_subroutes() if nav["route"] == route][0]


def get_subitems_for_route(route):
    return [nav for nav in nav_items if nav["route"] == route][0]["subitems"]


nav_items = [
    {"route": "summary", "title": _("Project Summary"), "explanation": _(
        "A discussion of the Radical Empiricism Project, in which the advantages of a multidimensional tensor analysis of metaphorical manifolds is dimensionaland the errors of unidimensional assertions of rank are critiqued"),
     "subitems": [
         {"route": "objective", "title": _("Objective"), "explanation": _("Objective")},
         {"route": "two_dimensional", "title": _("Two-Dimensional Polar Relations and Two-by-Two Matrices"),
          "explanation": _("Two-Dimensional Polar Relations and Two-by-Two Matrices")},
         {"route": "flat", "title": _("The flat space of totality"), "explanation": _("The flat space of totality")},
         {"route": "three", "title": _("Three-Dimensional Analysis"), "explanation": _("Three-Dimensional Analysis")},
     ]},
    {"route": "genre_theory", "title": _("Theory of Genre Sets"), "explanation": _(
        "This page features many discussion: (1) An Introduction to Genre Sets, (2) An example analysis of a sentence from Totality and Infinity as a constellation of Genre Sets, (3) Genre Set Membership Rules [suffixes, prefixes, etymological roots, infinities, other morphemic roots, semantic themes], (4)Internal and External Relations [duality, combination, repetition, opposition, intersection], (5) Non-Euclidean Relations [parallelism, flat, two_dimensional, constellation, curvature ], (5) Other mathematical and scientific topics [addition, positive, negative, 0, 1, 2, 3, 4, infinity, set theory, continuity and infinitesimals, topology, Mikowski/Einstein space-time, wave and quantum theory  ] (6) Perspectivism [perversion, inversion, subversion, reversion] (7) Reading Totality and Infinity as Genesis and Otherwise than Being as Exodus"),
     "subitems": [
         {"route": "constellation_example", "title": _("Constellational Analysis of a Kallidescopic Sentence"),
          "explanation": _("Constellational Analysis of a Kallidescopic Sentence")},
         {"route": "membership", "title": _("Group Set Membership"), "explanation": _("")},
         {"route": "abstract", "title": _("Abstract"), "explanation": _("")},
         {"route": "genre_set_intro", "title": _("Introduction to Genre Sets"), "explanation": _("")},
         {"route": "combination", "title": _("Combination"), "explanation": _("")},
         {"route": "repetition", "title": _("Repetition"), "explanation": _("")},
         {"route": "opposition", "title": _("Opposition"), "explanation": _("")},
         {"route": "intersection", "title": _("Intersection"), "explanation": _("")},
         {"route": "parallelism", "title": _("Parallelism"), "explanation": _("")},
         {"route": "flat", "title": _("Flat"), "explanation": _("")},
         {"route": "two_dimensional", "title": _("Two Dimensional"), "explanation": _("")},
         {"route": "curvature", "title": _("Curvature"), "explanation": _("")},
         {"route": "numbers", "title": _("Numbers"), "explanation": _("")},
         {"route": "addition", "title": _("Addition"), "explanation": _("")},
         {"route": "perspectivism", "title": _("Perspectivism"), "explanation": _("")},
         {"route": "zero", "title": _("Zero"), "explanation": _("")},
         {"route": "one", "title": _("One"), "explanation": _("")},
         {"route": "duality", "title": _("Duality"), "explanation": _("")},
         {"route": "trois", "title": _("Trois"), "explanation": _("")},
         {"route": "three", "title": _("Three"), "explanation": _("")},
         {"route": "four", "title": _("Four"), "explanation": _("")},
     ]},
    {"route": "mots", "title": _("Word list"), "explanation": _(
        "A list of all 16000 words in both Totality and Otherwise. Links to information pages about each word, including definitions and etymologies in English and French, as well as frequencies and lines from both texts")},
    {"route": "genres", "title": _("List of Genre Sets"), "explanation": _("A list of Genre Sets.")},
    {"route": "technical", "title": _("Technical notes"),
     "explanation": _("Contact information, sources, current project status and future direction")},
]

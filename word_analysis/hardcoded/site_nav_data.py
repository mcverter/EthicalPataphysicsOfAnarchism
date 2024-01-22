from django.utils.translation import gettext as _


def get_subitems(route):
    return [nav for nav in nav_items if nav["route"] == route][0]["subitems"]


nav_items = [
    {"route": "summary", "title": _("Project Summary"), "explanation": _(
        "A discussion of the Radical Empiricism Project, in which the advantages of a multidimensional tensor analysis of metaphorical manifolds is dimensionaland the errors of unidimensional assertions of rank are critiqued"),
     "subitems": [
         {"route": "objective", "title": _("Objective"), "explanation": _("Objective")},
         {"route": "two_dimensional", "title": _("Two-Dimensional Polar Relations and Two-by-Two Matrices"),
          "explanation": _("Two-Dimensional Polar Relations")},
         {"route": "flat", "title": _("The flat space of totality"), "explanation": _("The flat space of totality")},
         {"route": "three", "title": _("Three-Dimensional Analysis"), "explanation": _("Three-Dimensional Analysis")},
     ]},
    {"route": "genre_theory", "title": _("Theory of Genre Sets"), "explanation": _(
        "This page features many discussion: (1) An Introduction to Genre Sets, (2) An example analysis of a sentence from Totality and Infinity as a constellation of Genre Sets, (3) Genre Set Membership Rules [suffixes, prefixes, etymological roots, infinities, other morphemic roots, semantic themes], (4)Internal and External Relations [duality, combination, repetition, opposition, intersection], (5) Non-Euclidean Relations [parallelism, flat, two_dimensional, constellation, curvature ], (5) Other mathematical and scientific topics [addition, positive, negative, 0, 1, 2, 3, 4, infinity, set theory, continuity and infinitesimals, topology, Mikowski/Einstein space-time, wave and quantum theory  ] (6) Perspectivism [perversion, inversion, subversion, reversion] (7) Reading Totality and Infinity as Genesis and Otherwise than Being as Exodus"),
     "subitems": [
         {"route": "#constellation_example", "title": _(""), "explanation": _("")},
         {"route": "#content_card", "title": _(""), "explanation": _("")},
         {"route": "#abstract", "title": _(""), "explanation": _("")},
         {"route": "#genre_set_intro", "title": _(""), "explanation": _("")},
         {"route": "#duality", "title": _(""), "explanation": _("")},
         {"route": "#combination", "title": _(""), "explanation": _("")},
         {"route": "#repetition", "title": _(""), "explanation": _("")},
         {"route": "#opposition", "title": _(""), "explanation": _("")},
         {"route": "#intersection", "title": _(""), "explanation": _("")},
         {"route": "#parallelism", "title": _(""), "explanation": _("")},
         {"route": "#flat", "title": _(""), "explanation": _("")},
         {"route": "#two_dimensional", "title": _(""), "explanation": _("")},
         {"route": "#constellation", "title": _(""), "explanation": _("")},
         {"route": "#curvature", "title": _(""), "explanation": _("")},
         {"route": "#numbers", "title": _(""), "explanation": _("")},
         {"route": "#addition", "title": _(""), "explanation": _("")},
         {"route": "#perversion", "title": _(""), "explanation": _("")},
         {"route": "#inversion", "title": _(""), "explanation": _("")},
         {"route": "#subversion", "title": _(""), "explanation": _("")},
         {"route": "#reversion", "title": _(""), "explanation": _("")},
         {"route": "#perspectivism", "title": _(""), "explanation": _("")},
         {"route": "#zero", "title": _(""), "explanation": _("")},
         {"route": "#one", "title": _(""), "explanation": _("")},
         {"route": "#trois", "title": _(""), "explanation": _("")},
         {"route": "#three", "title": _(""), "explanation": _("")},
         {"route": "#four", "title": _(""), "explanation": _("")},
     ]},
    {"route": "mots", "title": _("Word list"), "explanation": _(
        "A list of all 16000 words in both Totality and Otherwise. Links to information pages about each word, including definitions and etymologies in English and French, as well as frequencies and lines from both texts")},
    {"route": "genres", "title": _("List of Genre Sets"), "explanation": _("A list of Genre Sets.")},
    {"route": "technical", "title": _("Technical notes"),
     "explanation": _("Contact information, sources, current project status and future direction")},
]

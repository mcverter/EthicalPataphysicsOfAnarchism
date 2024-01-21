from django.utils.translation import gettext as _

nav_items = [
    {"route": "summary", "title": _("Project Summary"), "explanation": _(
        "A discussion of the Radical Empiricism Project, in which the advantages of a multidimensional tensor analysis of metaphorical manifolds is dimensionaland the errors of unidimensional assertions of rank are critiqued")},
    {"route": "genre_theory", "title": _("Theory of Genre Sets"), "explanation": _(
        "This page features many discussion: (1) An Introduction to Genre Sets, (2) An example analysis of a sentence from Totality and Infinity as a constellation of Genre Sets, (3) Genre Set Membership Rules [suffixes, prefixes, etymological roots, infinities, other morphemic roots, semantic themes], (4)Internal and External Relations [duality, combination, repetition, opposition, intersection], (5) Non-Euclidean Relations [parallelism, flat, two_dimensional, constellation, curvature ], (5) Other mathematical and scientific topics [addition, positive, negative, 0, 1, 2, 3, 4, infinity, set theory, continuity and infinitesimals, topology, Mikowski/Einstein space-time, wave and quantum theory  ] (6) Perspectivism [perversion, inversion, subversion, reversion] (7) Reading Totality and Infinity as Genesis and Otherwise than Being as Exodus")},
    {"route": "mots", "title": _("Word list"), "explanation": _(
        "A list of all 16000 words in both Totality and Otherwise. Links to information pages about each word, including definitions and etymologies in English and French, as well as frequencies and lines from both texts")},
    {"route": "genres", "title": _("List of Genre Sets"), "explanation": _("A list of Genre Sets.")},
    {"route": "technical", "title": _("Technical notes"),
     "explanation": _("Contact information, sources, current project status and future direction")},
]

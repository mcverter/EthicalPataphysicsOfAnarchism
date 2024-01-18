import os
import re
from django.test import TestCase, Client
from .hardcoded.site_nav_data import nav_items

c = Client()


class RouteTests(TestCase):
    def route_test(self, route):
        if not route.startswith("/"):
            route = "/" + route
        response = c.get(route)
        print('route', route, 'response_code', response.status_code)
        assert response.status_code == 200 or response.status_code == 301, f"route {route} failed"

    def gather_all_routes(self, items):
        all_toproutes = [item["route"] for item in items]
        all_subroutes = [self.gather_all_routes(item["subitems"]) for item in items if "subitems" in item]
        print(all_subroutes)
        return sum(all_subroutes, all_toproutes)

    def z_test_nav_bar_routes(self):
        all_routes = self.gather_all_routes(nav_items)
        print(all_routes)
        for route in all_routes:
            self.route_test(route)

    def check_word_routes_in_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            all_matches = re.findall('/mot/\w+', content)
            for m in all_matches:
                print("testing route", m)
                self.route_test(m)

    def test_word_routes_in_objective_file(self):
        objective_file = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                      'templates/content/objective.html')
        self.check_word_routes_in_file(objective_file)


routes = [
    "",
    "words",
    "mots",
    "mot/etre",
    # "word/etre",
    # "mot/be",
    # "word/be",
    "genres",
    # "genre/GEOMETRIE",
    "abstract",
    "addition",
    "combination",
    "constellation",
    # "curvature",
    # "courbure",
    # "deux",
    "duality",
    # "two",
    # "euclid",
    "flat",
    "intersection",
    "numbers",
    "objective",
    "opposition",
    "parallelism",
    "two_dimensional",
]
untested = [
    "definition",
    "etymology",
    "un",
    "one",
    "zero",
    "null",
    "trois",
    "three",
    "perversion",
    "inversion",
    "subversion",
    "reversion",
    "quatre",
    "four",
    "square",
    "carre",
    "perspectivism",
    # TODO: move these to BCP
    "relations",
    "summary",
    "resume",
    "technical",
    "technique",
    "debug_test",
    # "mots/(?P<prefix>.*)/",

]

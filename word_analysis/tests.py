from django.test import TestCase, Client

c = Client()


class RouteTests(TestCase):
    def test_routes(self):
        for route in routes:
            print('route', route)
            response = c.get("/" + route)
            print('route', route, 'response_code', response.status_code)
            assert response.status_code == 200 or response.status_code == 301, f"route {route} failed"


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
import unittest
from ..e_populate__english_etymology import populate_english_etymology

expected = 'UPDATE WordAnalysis_word SET english_etymology = \'late 14c., realtif, in grammar, "a relative pronoun," from Old French relatif (13c.), from Late Latin relativus "having reference or relation," from Latin relatus, used as past participle of referre "bring back, bear back" (see refer), from re- "back, again" + lātus "borne, carried" (see oblate (n.)). The meaning "kinsman, kinswoman, person in the same family or connected by blood" is attested from 1650s.   \' WHERE english=\'foo\';\n'
class SqlUpdateTests(unittest.TestCase):
    def test_sql_update(self):
        self.assertEqual(populate_english_etymology(), expected)


if __name__ == '__main__':
    unittest.main()

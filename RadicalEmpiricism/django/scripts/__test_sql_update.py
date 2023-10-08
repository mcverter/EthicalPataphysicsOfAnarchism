import unittest
from write_sql__update_word_tbl__english_etymology import add_english_etymology

expected = 'late 14c., realtif, in grammar, "a relative pronoun," from Old French relatif (13c.), from Late Latin relativus "having reference or relation," from Latin relatus, used as past participle of referre "bring back, bear back" (see refer), from re- "back, again" + lātus "borne, carried" (see oblate (n.)). The meaning "kinsman, kinswoman, person in the same family or connected by blood" is attested from 1650s.   '
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(add_english_etymology(), expected)


if __name__ == '__main__':
    unittest.main()

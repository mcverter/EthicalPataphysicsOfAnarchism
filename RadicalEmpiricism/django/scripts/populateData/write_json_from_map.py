import os

dir_path = os.path.dirname(os.path.realpath(__file__))
word_map_path = os.path.join(dir_path, '../../data/books/WordMap.txt')
fixtures_path = os.path.join(dir_path, '../../WordAnalysis/fixtures/words.json')


def populate_words_from_map():
    output = '['

    with open(word_map_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            (french, ti, otb) = line.split(',')

            skip_words = ['d"qne', '"', "\\", 'j"a']
            if french is not None and french not in skip_words:
                french = french.strip()
                if french[-1] == '"':
                    french = french[:-1]
                if french[0] == '"':
                    french = french[1:]

                ti = ti.strip()
                otb = otb.strip()

                output += '{"model": "WordAnalysis.Word", "fields":{'
                output += f'''"french": "{french}","ti": {ti},"otb": {otb}'''
                output += '''}},'''

        # remove trailing comma
        output = output[:-1]

    output += ']'
    with open(fixtures_path, "w", encoding="utf-8") as g:
        g.write(output)


populate_words_from_map()

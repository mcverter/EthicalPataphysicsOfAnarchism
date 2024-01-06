from constants import (OTB_FULL_FRENCH_TITLE, OTB_FULL_ENGLISH_TITLE, TI_FULL_FRENCH_TITLE, \
                       TI_FULL_ENGLISH_TITLE, OTB_SHORT_FRENCH_TITLE, OTB_SHORT_ENGLISH_TITLE, TI_SHORT_FRENCH_TITLE,
                       TI_SHORT_ENGLISH_TITLE, \
                       TI, OTB, SITE_ENGLISH_ETYMOLOGY_URL, SITE_FRENCH_ETYMOLOGY_URL, SITE_FRENCH_ETYMOLOGY_NAME,
                       SITE_ENGLISH_DEFINITIONS_NAME, SITE_FRENCH_DEFINITIONS_URL, SITE_FRENCH_DEFINITIONS_NAME,
                       SITE_ENGLISH_DEFINITIONS_URL, SITE_ENGLISH_ETYMOLOGY_NAME)


def messages_context(request):
    messages = {
        "no_value_yet_en": "No Value Yet",
        "no_value_yet_fr": "Aucun result"
    }
    return {"sysmsg": messages}


def title_context(request):
    sources = {
        "definition": {
            "french": {
                "url": SITE_FRENCH_DEFINITIONS_URL,
                "name": SITE_FRENCH_DEFINITIONS_NAME,
            },
            "english": {
                "url": SITE_ENGLISH_DEFINITIONS_URL,
                "name": SITE_ENGLISH_DEFINITIONS_NAME
            }
        },
        "etymology": {
            "french": {
                "url": SITE_FRENCH_ETYMOLOGY_URL,
                "name": SITE_FRENCH_ETYMOLOGY_NAME,
            },
            "english": {
                "url": SITE_ENGLISH_ETYMOLOGY_URL,
                "name": SITE_ENGLISH_ETYMOLOGY_NAME,
            }
        }
    }

    titles = {
        TI: {
            "short": {
                "french": TI_SHORT_FRENCH_TITLE,
                "english": TI_SHORT_ENGLISH_TITLE
            },
            "long": {
                "french": TI_FULL_FRENCH_TITLE,
                "english": TI_FULL_ENGLISH_TITLE
            }
        },

        OTB: {
            "short": {
                "french": OTB_SHORT_FRENCH_TITLE,
                "english": OTB_SHORT_ENGLISH_TITLE
            },
            "long": {
                "french": OTB_FULL_FRENCH_TITLE,
                "english": OTB_FULL_ENGLISH_TITLE
            }
        }

    }
    return {"titles": titles, "sources": sources}


'''
 count = len(Foo.objects.filter(user = request.user))
+  return {"foo_count" :count}
'''

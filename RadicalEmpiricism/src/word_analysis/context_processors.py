from RadicalEmpiricism.src.constants import OTB_FULL_FRENCH_TITLE, OTB_FULL_ENGLISH_TITLE, TI_FULL_FRENCH_TITLE, TI_FULL_ENGLISH_TITLE, \
    OTB_SHORT_FRENCH_TITLE, OTB_SHORT_ENGLISH_TITLE, TI_SHORT_FRENCH_TITLE, TI_SHORT_ENGLISH_TITLE, \
    TI, OTB

def messages_context(request):
    messages = {
        "no_value_yet_en": "No Value Yet",
        "no_value_yet_fr": "Aucun result"
    }
    return {"sysmsg": messages}
def title_context(request):
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
    return {"titles": titles}


'''
 count = len(Foo.objects.filter(user = request.user))
+  return {"foo_count" :count}
'''

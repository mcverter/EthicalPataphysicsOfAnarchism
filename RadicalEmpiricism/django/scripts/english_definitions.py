from english_dictionary.scripts.read_pickle import get_dict
english_dict = get_dict()

definition = english_dict["xylophone"]  # english_dict is a Python dictionary of English
print(definition)
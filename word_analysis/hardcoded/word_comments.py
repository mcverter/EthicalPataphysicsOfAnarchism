def word_comments(word=''):
    if not word:
        return ALL_WORD_COMMENTS
    return ALL_WORD_COMMENTS[word]


def all_words_to_categories():
    word_to_category_dict = {}
    for category, words in ALL_WORD_COMMENTS:
        for word in words:
            if word not in word_to_category_dict:
                word_to_category_dict[word] = []
            word_to_category_dict[word].append(category)

    return word_to_category_dict


ALL_WORD_COMMENTS = {
    "origine": "the intersection of time, space, and birth",
    "tenir": ""
}

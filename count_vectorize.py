#!/usr/bin/python

def term_freq(text):

    word_data = [text]

    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer(min_df=1)
    bag = vectorizer.fit_transform(word_data)
    feature_names = vectorizer.get_feature_names()
    doc = 0
    feature_index = bag[doc,:].nonzero()[1]
    freq = zip(feature_index, [bag[doc, x] for x in feature_index])

    score_dic = {}

    for w, s in [(feature_names[i], s) for (i, s) in freq]:
        score_dic.update({w: s})

    return score_dic

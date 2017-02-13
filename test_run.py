import os
import string
import math
import string
import files_read
import wordpositionlist
import dist_bet_words
import count_vectorize
import check_named_entity
import check_noun_phrase


all_text = ["my name is Anup it is", "is Divyansh Goel in an working ass hole ass Divyansh", "is this working right this"]

dic_arr = files_read.id_words(all_text)
print dic_arr

#print files_read.feat_arr(wordpositionlist.wordpos, all_text, dic_arr)


#score_dic = [count_vectorize.term_freq(text) for text in all_text]
#print score_dic
#print files_read.feat_arr(count_vectorize.term_freq, all_text, dic_arr)

#nameentity_dic = [check_named_entity.checkNamedEntities(text) for text in all_text]
#nameentity_arr = files_read.feat_arr(check_named_entity.checkNamedEntities, all_text, dic_arr)
#print nameentity_arr

#nounphrase_dic = [check_noun_phrase.checkNounPhrases(text) for text in all_text]
#nounphrase_arr = files_read.feat_arr(check_noun_phrase.checkNounPhrases, all_text, dic_arr)
#print nounphrase_dic
#print nounphrase_arr




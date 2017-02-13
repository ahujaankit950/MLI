import os
import string
import math
import string
import files_read
import wordpositionlist
import count_vectorize
import check_named_entity
import check_noun_phrase
import wordpositionlist
import distbetwords
import get_word_length
import tfidf
import capitalisation
import wikifreq


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

#wordpos_dic = [wordpositionlist.wordpos(text) for text in all_text]
#wordpos_arr = files_read.feat_arr(wordpositionlist.wordpos, all_text, dic_arr)
#print wordpos_dic
#print wordpos_arr

#distrms_dic = [distbetwords.disBetWords(text) for text in all_text]
#distrms_arr = files_read.feat_arr(distbetwords.disBetWords, all_text, dic_arr)
#print distrms_dic
#print distrms_arr

#wordlen_dic = [get_word_length.getWordLength(text) for text in all_text]
#wordlen_arr = files_read.feat_arr(get_word_length.getWordLength, all_text, dic_arr)
#print wordlen_dic
#print wordlen_arr

#tfidf_dic = tfidf.tfidFreq(all_text) 		#not like all others !special attention req
#tfidf_arr = tfidf.tfidf_arr(all_text, dic_arr)
#print tfidf_dic
#print tfidf_arr

#caps_dic = [capitalisation.capitalWords(text) for text in all_text]
#caps_arr = files_read.feat_arr(capitalisation.capitalWords, all_text, dic_arr)
#print caps_dic
#print caps_arr

#wiki_dic = [wikifreq.wikifrequncy(text) for text in all_text]
#wiki_arr = files_read.feat_arr(wikifreq.wikifrequncy, all_text, dic_arr)
#print wiki_dic
#print wiki_arr


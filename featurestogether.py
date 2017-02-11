#getting all featurestogether

import os
import string
import math
import string
import files_read
import dist_bet_words


path = r"C:\Users\ANUP\Documents\GitHub\MLI\test.txt"
text = files_read.read_file(path)
pro = files_read.remove_punct(text)
list = pro.split()
dist_dic = dist_bet_words.dist_bet_words(list)
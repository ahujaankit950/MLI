#!/usr/bin/python

import os
import pickle
import re
import sys
import numpy as np

sys.path.append("../text_learning/")


f_list  = open("..\\add1.txt", "r")


from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0
n = 0
names_list = []

for path in f_list:
    ### only look at first 200 emails when developing
    ### once everything is working, remove this line to run over full dataset
    
    if temp_counter < 100:
            temp_counter += 1
            path = os.path.join('..', path[:-1])
            print path
            email = open(path, "r")
                
            ### use parseOutText to extract the text from the opened email
            #parsed_email = parseOutText(email)
            email.seek(0)  ### go back to beginning of file (annoying)
            all_text = email.read()
            content = all_text
            words = ""
            if len(content) > 1:
                text_string = content.translate(string.maketrans("", ""), string.punctuation)
                
            word_data.append(text_string)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
                  
            n += 1

            email.close()

            names = getNamedEntities(path)
            for x in names:
                names_list.append(x)
        
print n, "emails processed"

for email in word_data:
    

    
    




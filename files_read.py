import os
import string
import numpy

def add_read(path):
	all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	emails = [mail for mail in all_files if (mail.endswith('.txt')) and not mail.endswith('justTitle.txt')]
	#print emails
	adds = [os.path.join(path, x) for x in emails]
	#print adds
	return adds



add_read("C:\\Users\\ANUP\\Documents\\machine_learning\\datasets\\500N-KPCrowd-v1.1\\CorpusAndCrowdsourcingAnnotations\\train")

def read_file(path):
	f = open(path, "r")
	f.seek(0)
	cont = f.read()
	f.close()
	return cont

def read_all(adds):
	all_text = []
	for path in adds:
		cont = read_file(path)
		all_text.append(cont)
		
	return all_text

def remove_punct(str):
	text = str.translate(string.maketrans("", ""), string.punctuation)
	return text

def id_words(all_text):
	mail = 0
	iden = 0
	ar = []
	for mail in all_text:
		words = [word for word in mail.split()]
		words.sort()
		dic = {}
		for word in words:
			if word not in dic.keys():
				dic.update({word: iden})
				iden = iden + 1
		ar.append(dic)
	return ar

#text = ["text is data type data", "hitesh chutiya hai hitesh", "divyansh is an working ass hole ass" ]
#ar = id_words(text)




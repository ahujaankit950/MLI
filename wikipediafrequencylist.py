# finds the wikipedia frequency
# feature= wikifrequncy
#import wikiwords

def wikifrequncy(file) :
    list = file.split()
    dict = {}
    for i in range(len(list)) :
        word = list[i]
        if not word in dict :
            dict[word] = wikiwords.freq(word)
    return dict
    
def fun(mails,arrK) :               #mails is list of mails(string), arrk is array of dict of every mail containing words and id
    mailNo=0
    listO = []
    for mail in mails :
        file = mail.split()
        dict = wikifrequncy(mail)
        for word in file :
            dict1 = arrK[mailNo]
            key = dict1[word]
            list1 = [mailNo,key,dict[word]]
            listO.append(list1)
        mailNo = mailNo+1
    return listO                          #listO of the form:- [mailno,key,feature]
    
    
'''
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

text = ["text hai ki Anup chUtiys Hai", "anup bhosDika Madarchod bina LunD KA", "CHUT pHati KA hai anup" ]
ar = id_words(text)
print ar
print fun(text,ar)
'''







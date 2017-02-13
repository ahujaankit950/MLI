# finds the distance between words
# feature= words distance

def addword(dict,word) :
    if not word in dict :
        dict[word] = []
        
def finddistance(word,index,list) :
    try :
        next = list.index(word,index+1)
      # print "next element at: ",next
        return next-index
    except :
        return 0

def adddistance(distance,dict,word) :
    l = dict[word]
    if distance != 0 :
        l.append(distance)

def Distance(file) :  #file is a string
    list = file.split()
    dict = {}
    i = 0
    while i<len(list) :
    # print "for the word :",word
        index = i
        word = list[i]
    #  print "index is: ",index
        addword(dict,word)
    #  print "after adding to dict:",dict
        distance = finddistance(word,index,list)
    #  print "distance bw words: ",distance
        adddistance(distance,dict,word)
    #   print "after loop dict: ",dict
        i = i+1
    return dict
    
def fun(mails,arrK) :               #mails is list of mails(string), arrk is array of dict of every mail
    mailNo=0
    listO = []
    for mail in mails :
        file = mail.split()
        dict = Distance(mail)
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

text = ["text hai ki Anup chUtiys Hai hai Anup ki text hai hai hai chUtiya gandu gandu", "anup bhosDika Madarchod phir se anup loda bhosDika bina LunD KA also also", "CHUT pHati KA hai anup KA CHUT pHati" ]
ar = id_words(text)
print ar
print fun(text,ar)
'''








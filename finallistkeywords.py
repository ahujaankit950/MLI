# fuction returns a final list where if a word is a keyword its value is 1 otherwise its 0

def function(dict,dictkey,flist) :
    indict = {v: k for k, v in dict.iteritems()}
    for key in sorted(indict.iterkeys()): 
        i=0
    for word in indict :
        if indict[word] in dictkey :
            flist.append(1)
        else :
            flist.append(0)

def finallist(keylist,arr) :      #keylist is list of dict{keyword:id} and arr is array of dict{word:key}
    flist = []
    for i in range(len(arr)) :
        dict = arr[i]
        dictkey = keylist[i]
        function(dict,dictkey,flist)
    return flist
    
'''   
def id_words(all_text):      #alltext list of mails
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
    
    
allkeys = ["hitesh Anup ki whats","bhosDika bina anup KA hello","from the other CHUT hai"]
text = ["text hai ki Anup chUtiys Hai", "anup bhosDika Madarchod bina LunD KA", "CHUT pHati KA hai anup" ]
ar = id_words(text)
print ar
print finallist(allkeys,ar)
'''

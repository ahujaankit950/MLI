'''
def add_read(path):
	all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	emails = [mail for mail in all_files if (mail.endswith('.keys'))]
	#print emails
	adds = [os.path.join(path, x) for x in emails]
	#print adds
	return adds
    
adds = add_read("C:\\Users\\ANUP\\Documents\\machine_learning\\datasets\\500N-KPCrowd-v1.1\\CorpusAndCrowdsourcingAnnotations\\train")

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

'''
    
    
def check(keyword,dick) :     #keyword is a string dick is a dict
    list = keyword.split()
    dict = {}
    for i in range(len(list)) : 
        if list[i] in dick :
            dict[list[i]] = dick[list[i]]
    return dict
    

def keywords(alltext,ar) :    #returns a list of dict {keyword:id}  #ar is a array of dict{word:id} #alltext is a list of textfiles containing keywords
    list = []
    for i in range(len(ar)) :
        dick = check(alltext[i],ar[i])    #dick is a dict of {keyword:id}
        list.append(dick)
    return list
    
''' 
   
#allkeys = read_all(adds)          #allkeys is a list of textfile of keywords
allkeys = ["hitesh Anup ki whats","bhosDika bina anup KA hello","from the other CHUT hai"]
text = ["text hai ki Anup chUtiys Hai", "anup bhosDika Madarchod bina LunD KA", "CHUT pHati KA hai anup" ]
ar = id_words(text)
print ar
print keywords(allkeys,ar)

'''

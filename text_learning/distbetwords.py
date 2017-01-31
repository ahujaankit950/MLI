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

f = open("test.txt","r")
file = f.read()
file = ''.join([c for c in file if c not in ('!', '?' )])  # this line removes punctuation , add punctuations in the bracket 
list = file.split()
# print "list is: ",list
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
    
print dict

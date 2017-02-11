# word position-1st position

def wordpos(file) :
    list = file.split()
    dict = {}

    for i in range(len(list)) :
        word = list[i]
        if not word in dict :
            dict[word] = i+1
    return dict

def fun(mails,arrK) :               #mails is list of mails(string), arrk is array of dict of every mail
    mailNo=0
    listO = []
    for mail in mails :
        file = mail.split()
        dict = wordpos(mail)
        for word in file :
            dict1 = arrK[mailNo]
            key = dict1[word]
            list1 = [mailNo,key,dict[word]]
            listO.append(list1)
        mailNo = mailNo+1
    return listO                          #listO of the form:- [mailno,key,feature]

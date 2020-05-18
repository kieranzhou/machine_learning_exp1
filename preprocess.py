import re
import os
#-----------------------------------------step0 prepare all the textfile--------------------------------------------------------------------------------------------
train_dir = r'.\dataset\20news-bydate\20news-bydate-train'
dic = []
# print(os.listdir(train_dir))
# root_dir = r'.\dataset\20news-bydate\20news-bydate-train\comp.os.ms-windows.misc'
# print(os.path.abspath(root_dir))
# print(os.listdir(root_dir))
for train_var in os.listdir(train_dir):
    print(len(dic))
    temp_dir = train_dir + '\\' + train_var
    for data_file in os.listdir(temp_dir):
        file_addr = temp_dir + '\\' + data_file
        # read file and cutting head
        fp = open(file_addr, encoding='gb18030', errors = 'ignore') #tag:maybe error later
        lines = fp.readlines()
        fp.close()
        head = 0
        for item in enumerate(lines):
            # print(item[1][0:5])
            if item[1][0:5].strip() == 'Lines': 
                head = item[0]
                break
        del lines[0:head+1]
        # splitting the words
        # print(lines)
        for sentence in lines:
            temp_list = list(filter(None, re.split(r'[0-9!:@#$%^&*?/<>,.+=_;|{}~`\-\s\n\(\)\\\'\[\]\"]\s*', sentence)))
            for word in temp_list:
                if word == '':
                    continue
                if word not in dic:
                    dic.append(word)
# finish and minimize and deliminate
for i in range(0,len(dic)):
    dic[i] = dic[i].lower()
dic = (list(set(dic)))
dic.sort()#bad idea

# delete stopword
fp = open('stopwords.txt')
try:
    alltext = fp.read()
    # print(alltext)
finally:
    fp.close()
stop_list = alltext.split('\n')
# print(stop_list)
temp = 0
for i in range(0, len(dic)):
    if dic[temp] in stop_list:
        del dic[temp]
    else:  
        temp += 1
print (dic)
stat_dic = []
for i in range(0, len(dic)):
    stat_dic.append([dic[i], i])
print(stat_dic)

f = open("Dictionary.txt",'a')
for item in stat_dic:
    f.write(strcontent)
    f.write('\n')
f.close






"""         
cutting head, spliting the words altogether and then lowerrize and deliminate
it is about the space and the time
 """






""" 
#-----------------------------------------step1 cut the head--------------------------------------------------------------------------------------------
fp = open('37915')
lines = fp.readlines()
#print(lines)
fp.close()
head = 0
for item in enumerate(lines):
#    print(item[1][0:5])
    if item[1][0:5].strip() == 'Lines':
        head = item[0]
        break
del lines[0:head+1]
#print(lines)


#-----------------------------------------step2 split it up and deleting--------------------------------------------------------------------
print ("step2-------------------------------------------------\n")
dic = []
for item in lines:
    temp_list = list(filter(None, re.split(r'[!@#$%^&*?\-,.\s\n\(\)]\s*', item)))
    # please remeber there is a ......issue
    # print(temp_list)
    for word in temp_list:
        if word == '':
            continue
        if word not in dic:
            dic.append(word)
print(dic)


#-----------------------------------------step3 lowerize the characters--------------------------------------------------------------------
print ("step3-------------------------------------------------\n")
for i in range(0,len(dic)):
    dic[i] = dic[i].lower()
dic = (list(set(dic)))
# can't use the sort directly in the above line.
dic.sort()#bad idea
print(dic)


#-----------------------------------------step4 dealing with the stopwords--------------------------------------------------------------------
print ("step 4-----------------------------------------------\n")

fp = open('stopwords.txt')
try:
    alltext = fp.read()
    # print(alltext)
finally:
    fp.close()
stop_list = alltext.split('\n')
# print(stop_list)
temp = 0
for i in range(0, len(dic)):
    if dic[temp] in stop_list:
        del dic[temp]
    else:  
        temp += 1
print (dic)

//AFTER PREPROCESS


 """





#-----------------------------------------preparing the stopwords list----------------------------------------------------------
'''
fp = open('stopwords.txt')
try:
    alltext = fp.read()
    print(alltext)
finally:
    fp.close()
stop_list = alltext.split('\n')
print(stop_list)

'''
#------------------------------------------testing the split and resplit--------------------------------------------------
'''
temp = "like me anyway!"
temp_list = list(filter(None, re.split(r'[;,\s!]\s*', temp)))
#temp_list = temp.split(' ')
print(temp_list)
sentence = "are you love me or hate me anyway bitch like "
sentence_list = sentence.split(' ')
print(sentence_list)
output = []
for w in sentence_list:
    if w in temp_list:
        output.append(w)
#output = [w for w in sentence_list if w in temp_list]
print(output)
'''

#------------------------------------------the original module------------------------------------------
'''
print(temp.split())
print(temp)
print("hello world")
'''
'''
sentence = "this is a apple"
filter_sentence= [w for w in sentence.split(' ') if w not in stopwords.words('english')]
print(filter_sentence)
'''
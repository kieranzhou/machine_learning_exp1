# to caculate the frequency, Li told us to use tf-idf to represent the frequency instead of the normal frequency
# term frequency is the number of times a term occurs in a document
# inverse document frequency is the logarithmically scaled inverse fraction of the documents that contain the 
# word (obtained by dividing the total number of documents by the number of documents containing the term, and 
# then taking the logarithm of that quotient)

# make another tf-idf to represent the importance of each word

# term frequency------------------------------------------------------------------------------------------------
import re
import os
import math

#----------------------------------------------------------------------------------------------------------------------
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros
#-----------------------------------------step0 prepare all the textfile--------------------------------------------------------------------------------------------
train_dir = r'.\dataset\20news-bydate\20news-bydate-train'
stat_dic = []   #need to change the global dic
fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
for line in fp.readlines():
    stat_dic.append(line.strip('\n'))
fp.close()
documents = []  #saving the info
for train_var in os.listdir(train_dir):
    varis = []   #each document saves each document's feature
    temp_dir = train_dir + '\\' + train_var
    for data_file in os.listdir(temp_dir):
        file_features = []#each file feature init
        file_addr = temp_dir + '\\' + data_file
        fp = open(file_addr, encoding='gb18030', errors = 'ignore') #tag:maybe error later
        lines = fp.readlines()
        fp.close()
        head = 0
        for item in enumerate(lines):
            if item[1][0:5].strip() == 'Lines': 
                head = item[0]
                break
        del lines[0:head+1]
        temp_dic = []
        for sentence in lines:
            temp_list = list(filter(None, re.split(r'[0-9!:@#$%^&*?/<>,.+=_;|{}~`\-\s\n\(\)\\\'\[\]\"]\s*', sentence)))
            for word in temp_list:
                if word not in temp_dic:
                    temp_dic.append(word)
        for i in range(0, len(temp_dic)):
            temp_dic[i] = temp_dic[i].lower()
        # temp_dic = list(set(temp_dic))
        temp_dic.sort()
        forsearch = []
        for token in temp_dic:
        # the global map is from the stat_dic, however i want to use the hashmap as the pdf said, but i searched for the hashmap
        #and eventually it seems that the dic format is quite like the hashmap and it's the bucket sort.
        # the basic map is based on each document
            if token in stat_dic:
                if token in forsearch:
                    file_features[forsearch.index(token)][1] += 1
                    continue
                temprary_feature = [stat_dic.index(token), 1]
                forsearch.append(token)
                file_features.append(temprary_feature)
        file_features.append(len(temp_dic))
        varis.append(file_features)
    varis.append([len(os.listdir(train_dir)), train_var])
    documents.append(varis)

# next step = idf-----------------------------------------------------------------------------------------
# by using the temprary_feature to form the tf-idf
# the data structure of document_feature is (order, tf, tf-idf)
document_feature = []           
for var in documents:
    var_leng = var[-1][0]
    idf = zerolistmaker(len(stat_dic))
    for doc in var:
        length = doc[-1]
        for feat in doc:
            feat[1] = feat/length       #calculate the tf
            idf[feat[0]] += 1           #prepare the idf
    for i in idf:
        if i != 0:
            idf[i] = math.log(var_leng/idf[i], 10)
    for doc in var:
        for feat in doc:
            feat.append(idf[feat[0]])   #property idf
            feat.append(idf[feat[0]] * feat[1]) #tf-idf frequency
# last step = sparse coding-------------------------------------------------------------------------------
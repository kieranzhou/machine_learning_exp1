# term frequency------------------------------------------------------------------------------------------------
import re
import os
import math
import sys
import time
#----------------------------------------------------------------------------------------------------------------------
def zerolistmaker(n):
    listofzeros = [0] * n
    # print(type(listofzeros))
    return listofzeros
#-----------------------------------------step0 prepare all the textfile--------------------------------------------------------------------------------------------
def frequencymker(flag1):
    if flag1 == 0:
        traget_dir = r'.\dataset\20news-bydate\20news-bydate-train'
    else:
        traget_dir = r'.\dataset\20news-bydate\20news-bydate-test'
    stat_dic = []   #need to change the global dic
    fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
    for line in fp.readlines():
        stat_dic.append(line.strip('\n'))
    fp.close()
    documents = []  #saving the info
    for train_var in os.listdir(traget_dir):
        time_start = time.time()
        varis = []   #each document saves each document's feature
        doc_dir = traget_dir + '\\' + train_var
        for data_file in os.listdir(doc_dir):
            file_features = []#each file feature init
            file_addr = doc_dir + '\\' + data_file
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
                    temprary_feature = [stat_dic.index(token), 1]           #so the num is about 0-N-1
                    forsearch.append(token)
                    file_features.append(temprary_feature)
            file_features.append(len(temp_dic))
            varis.append(file_features)
        varis.append([len(os.listdir(doc_dir)), train_var])
        documents.append(varis)
        time_end = time.time()
        print("having calculating the term frequency of " + train_var)
        print("time interval:" + str(time_end - time_start))
    documents.append(len(os.listdir(traget_dir)))

    # next step = idf-----------------------------------------------------------------------------------------
    # by using the temprary_feature to form the tf-idf
    # the data structure of document_feature is (order, tf, tf-idf)           
    for var in documents[0:-1]:
        var_leng = var[-1][0]
        idf = zerolistmaker(len(stat_dic))
        for doc in var[0:-1]:
            length = doc[-1]
            # for i in range(0, len(doc) - 1):
            for feat in doc[0:-1]:
                # doc[i][1] = doc[i][1]/length
                feat[1] = feat[1]/length       #calculate the tf
                idf[feat[0]] += 1               #prepare the idf
            # print(doc[-2])
        for i in range(0, len(idf)):
            if idf[i] != 0:
                idf[i] = math.log(var_leng/idf[i], 10)
        for doc in var[0:-1]:
            for feat in doc[0:-1]:
                feat.append(idf[feat[0]])   #property idf
                feat.append(idf[feat[0]] * feat[1]) #tf-idf frequency
        var_name = var[-1][1]
        print("after calculating the tf-ifd of" + var_name)
    # write the file----------------------------------------------------------------------------------------------
    if flag1 == 0:
        target_file = "train_frequency_bayes.txt"
    else:
        target_file = "test_frequency_bayes.txt"
    fp = open(target_file, 'w')
    vars_amts = documents[-1]
    for i in range(0, vars_amts):
        docs_amts = documents[i][-1][0]
        var_name = documents[i][-1][1]
        fp.write(var_name + ' ')
        fp.write(str(docs_amts) + ' ')
        for j in range(0, docs_amts):
            attrs_amts = len(documents[i][j]) - 1
            # attrs_amts = documents[i][j][-1]
            fp.write(str(attrs_amts) + ' ')
            for m in range(0, attrs_amts):
                fp.write(str(documents[i][j][m][0]) + ' ' + str(documents[i][j][m][1]) + ' ' + str(documents[i][j][m][2]) + ' ' + str(documents[i][j][m][3]) + ' ')
        fp.write('\n')
    fp.close()

frequencymker(0)
print("finish the train-data frequency built")
frequencymker(1)
print("finish the test-data frequency built")
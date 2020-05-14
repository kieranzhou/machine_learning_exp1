# to caculate the frequency, Li told us to use tf-idf to represent the frequency instead of the normal frequency
# term frequency is the number of times a term occurs in a document
# inverse document frequency is the logarithmically scaled inverse fraction of the documents that contain the 
# word (obtained by dividing the total number of documents by the number of documents containing the term, and 
# then taking the logarithm of that quotient)


# term frequency------------------------------------------------------------------------------------------------
import re
import os
#-----------------------------------------step0 prepare all the textfile--------------------------------------------------------------------------------------------
train_dir = r'.\dataset\20news-bydate\20news-bydate-train'
# using stat_dic
stat_dic = []
for train_var in os.listdir(train_dir):
    temp_dir = train_dir + '\\' + train_var
    for data_file in os.listdir(temp_dir):
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
            temp_dic[i] = temp_dic[i].lower
        temp_dic = list(set(temp_dic))
        temp_dic.sort()
        # passage_length = len(temp_dic)
        document_dic = []
        for token in temp_dic:
        # the global map is from the stat_dic
        # the basic map is based on each document
            for i in range(0, len(stat_dic)):
                if stat_dic[i][0] == token:
                
                break
print (dic)





# next step = idf-----------------------------------------------------------------------------------------
# last step = sparse coding-------------------------------------------------------------------------------
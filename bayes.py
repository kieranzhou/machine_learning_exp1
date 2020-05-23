# spliting into 3 programs:
# writing some content into 2 files
import re
import os

# step 1 read the train data and make the frequency
# step 2 read the dic
# step 3 calculate the amount of each number
# step 4 calculate the prior probability
# have done all of these in the other two files 

# step 5 read the test data and the prior_prob and then verify it 


stat_dic = []   #need to change the global dic
fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
for line in fp.readlines():
    stat_dic.append(line.strip('\n'))
fp.close()
print("have read the Dictionary")
dic_len = len(stat_dic)

data = []
counter = 0      #counter is for vars
with open('prior_prob.txt', 'r') as f:
    alldata = f.readlines()
    for temp_var in alldata:
        tmp_list = list(filter(None, re.split(r'[\s\n]\s*', temp_var)))
        data.append([])         #vars
        var_name = tmp_list[0]
        files_amt = int(tmp_list[1])
        temp_point = 2
        for i in range(0, dic_len):
            data[counter].append([])        #files
            # read 2 elements
            data[counter].append(int(tmp_list[temp_point + 1]))
            temp_point += 2
        data[counter].append([var_name, files_amt]) #adding files amount
        counter += 1
    data.append(counter)                            #adding vars amount


testingdata = []
counter = 0      #counter is for vars
with open('test_frequency_bayes.txt', 'r') as f:
    alldata = f.readlines()
    for temp_var in alldata:
        tmp_list = list(filter(None, re.split(r'[\s\n]\s*', temp_var)))
        testingdata.append([])         #vars
        var_name = tmp_list[0]
        files_amt = int(tmp_list[1])
        temp_point = 2
        for i in range(0, files_amt):
            testingdata[counter].append([])        #files
            characters_amt = int(tmp_list[temp_point])
            text_num = int(tmp_list[temp_point + 1])
            temp_point += 2
            for j in range(0, characters_amt):
                # read 2 elements
                two_elements = [int(tmp_list[temp_point]), int(tmp_list[temp_point + 1])]
                testingdata[counter][i].append(two_elements)
                temp_point += 2
            testingdata[counter][i].append([characters_amt, text_num]) #adding characters amount
        testingdata[counter].append([var_name, files_amt]) #adding files amount
        counter += 1
    testingdata.append(counter)                            #adding vars amount

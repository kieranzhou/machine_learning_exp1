# spliting into 3 programs:
# writing some content into 2 files
import re
import os
import math
# step 1 read the train data and make the frequency
# step 2 read the dic
# step 3 calculate the amount of each number
# step 4 calculate the prior probability
# have done all of these in the other two files 

# step 5 read the test data and the prior_prob and then verify it 

def checker(splitor, checklist, total):
    Pa = math.log(splitor[-1][1]/total)
    temp_calculator = 0
    temp_calculator += Pa
    for item in checklist:
        temp_calculator += item[1] * math.log(splitor[item[0]])
    return temp_calculator

stat_dic = []   #need to change the global dic
fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
for line in fp.readlines():
    stat_dic.append(line.strip('\n'))
fp.close()
print("have read the Dictionary")
dic_len = len(stat_dic)

data = []
counter = 0      #counter is for vars
total_train_file = 0
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
        total_train_file += files_amt
        counter += 1
    data.append(counter)                            #adding vars amount


testingdata = []
# total_train_file = 0
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
        # total_train_file += files_amt
        counter += 1
    testingdata.append(counter)                            #adding vars amount

#-------check----------------------------------------------------------------------------------------------------------
accurate = 0
for var in testingdata[0:-1]:
    var_name = var[-1][0]
    files_amt = var[-1][1]
    for i in range(0, files_amt):
        checklist = []
        attr_amt = var[i][-1][0]
        for j in range(0, attr_amt):
            attr_no = var[i][j][0]
            attr_frqcy = var[i][j][1]
            checklist.append([attr_no, attr_frqcy])
        # check 20 bayes to determine which one is the best
        max = -1
        max_name = ' '
        for var_splitor in data:
            temp = checker(var_splitor, checklist, total_train_file)
            if temp > max:
                max = temp
                max_name = var_splitor[-1][0]
        if max_name == var_name:
            accurate += 1    

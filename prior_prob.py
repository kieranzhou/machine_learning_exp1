import re
import os
def zerolistmaker(n):
    listofzeros = [0] * n
    # print(type(listofzeros))
    return listofzeros

data = []
counter = 0      #counter is for vars
with open('train_frequency_bayes.txt', 'r') as f:
    alldata = f.readlines()
    for temp_var in alldata:
        tmp_list = list(filter(None, re.split(r'[\s\n]\s*', temp_var)))
        data.append([])         #vars
        var_name = tmp_list[0]
        files_amt = int(tmp_list[1])
        temp_point = 2
        for i in range(0, files_amt):
            data[counter].append([])        #files
            characters_amt = int(tmp_list[temp_point])
            text_num = int(tmp_list[temp_point + 1])
            temp_point += 2
            for j in range(0, characters_amt):
                # read 2 elements
                two_elements = [int(tmp_list[temp_point]), int(tmp_list[temp_point + 1])]
                data[counter][i].append(two_elements)
                temp_point += 2
            data[counter][i].append([characters_amt, text_num]) #adding characters amount
        data[counter].append([var_name, files_amt]) #adding files amount
        counter += 1
    data.append(counter)                            #adding vars amount

stat_dic = []   #need to change the global dic
fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
for line in fp.readlines():
    stat_dic.append(line.strip('\n'))
fp.close()
print("have read the Dictionary")
dic_len = len(stat_dic)

new_data_structure = []
for var in data[0:-1]:
    temp_var = zerolistmaker(dic_len)
    var_name = var[-1][0]
    files_amt = var[-1][1]
    var_total_num = 0
    for i in range(0, files_amt):
        attr_amt = var[i][-1][0]
        file_total_num = var[i][-1][1]
        for j in range(0, attr_amt):
            temp_var[var[i][j][0]] += var[i][j][1]
        var_total_num += file_total_num
    for i in range(0, dic_len):
        temp_var[i] = (temp_var[i] + 1)/(var_total_num + files_amt) #smooth factor, default 1
    temp_var.append([var_name, files_amt])
    new_data_structure.append(temp_var)
new_data_structure.append(data[-1])
# writing

fp = open("prior_prob.txt", 'w')
vars_amts = new_data_structure[-1]
for i in range(0, vars_amts):
    file_amt = new_data_structure[i][-1][1]
    var_name = new_data_structure[i][-1][0]
    fp.write(var_name + ' ')
    fp.write(str(file_amt) + ' ')
    for j in range(0, dic_len):
        fp.write(str(j) + ' ' + str(new_data_structure[i][j]) + ' ')
    fp.write('\n')
fp.close()
# this file is for calculate the perceptron
# step1:read the file from frequency.txt----------------------------------------
import re
def zerolistmaker(n):
    listofzeros = [0] * n
    # print(type(listofzeros))
    return listofzeros

def vector_multi(w, x, b):
    length = x[-1]
    total = 0
    for i in range(0, length):
        temp = x[i][0]
        total += w[temp] * x[i][3]
    total += b
    return total

def adjustw(w, x, step, para):
    length = x[-1]
    for i in range (0, length):
        temp = x[i][0]
        w[temp] += step * x[i][3] * para
    return w


data = []
# empty_list = [] append(copy.deepcopy(empty_list))
counter = 0      #counter is for vars
with open('frequency.txt', 'r') as f:
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
            temp_point += 1
            for j in range(0, characters_amt):
                # read 4 element
                four_elements = [int(tmp_list[temp_point]), float(tmp_list[temp_point + 1]), float(tmp_list[temp_point + 2]), float(tmp_list[temp_point + 3])]
                data[counter][i].append(four_elements)
                temp_point += 4
            data[counter][i].append(characters_amt) #adding characters amount
        data[counter].append([var_name, files_amt]) #adding files amount
        counter += 1
    data.append(counter)                            #adding vars amount
# print(data[-1])                            
#part2: reading the dictionary--------------------------------------------------------------------------------------------------------------------------

stat_dic = []   #need to change the global dic
fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
for line in fp.readlines():
    stat_dic.append(line.strip('\n'))
fp.close()

#part3: preparing for the perceptron--------------------------------------------------------------------------------------------------------------------------

# creating n spliters, preparing the parameters
# the form is f(wx+b), init the w and b
var_amt = data[-1]
w = []
for i in range(0, var_amt):
    w.append(zerolistmaker(len(stat_dic)))
b = zerolistmaker(var_amt)
# define the learning_step and threshold, preset 0.1 and ?not sure
step = 0.01
threshold = 0.5
interval = 2
rate = 1
# preparing the presplitor-----------------------------------------------------------------------------------------------------------------------------------
for one_var in data[0:-1]:
    split_num = int(data.index(one_var))
    var_name = one_var[-1] [0]
    files_amt = one_var[-1][1]
    while(1):
        flag = 1
        for i in range(0, files_amt):
            # w*x+b
            for j in range(0, var_amt):
                if j == split_num:
                    continue
                if (vector_multi(w[split_num], one_var[i], b[split_num]) <= vector_multi(w[j], one_var[i], b[j])):
                    # adjust the w and b
                    w[split_num] = adjustw(w[split_num], one_var[i], step, 1)
                    w[j] = adjustw(w[j], one_var[i], step, -1)
                    b[split_num] += step
                    b[j] -= step
                    flag = 0
        if flag == 1:
            break
# presplitorfinish-------------------------------------------------------------------------------------------------------------------------------------------

# try till it satisfy the result or try serveral times and just have an well result
# step could be deliminate with the loop goes on.
# i thought it is the second option that could just be so-so answer. mix

#only for test------------------------------------------------------------------------------------------------------
for time in range(0, 200):
    for one_var in data[0:-1]:
        split_num = int(data.index(one_var))
        var_name = one_var[-1] [0]
        files_amt = one_var[-1][1]
        while(1):
            flag = 1
            for i in range(0, files_amt):
                # w*x+b
                for j in range(0, var_amt):
                    if j == split_num:
                        continue
                    if (vector_multi(w[split_num], one_var[i], b[split_num]) <= vector_multi(w[j], one_var[i], b[j])):
                        # adjust the w and b
                        print(vector_multi(w[split_num], one_var[i], b[split_num]))
                        print(vector_multi(w[j], one_var[i], b[j]))
                        w[split_num] = adjustw(w[split_num], one_var[i], step, 1)
                        w[j] = adjustw(w[j], one_var[i], step, -1)
                        b[split_num] += step / (time+1)
                        b[j] -= step / (time + 1)
                        flag = 0
            if flag == 1:
                break
timetosee = 0

# approxmately 100  and maybe we could successed it, but maybe it is too similar with the train data
# adjusting the parameter is the most important affair now.


# making a checking function
for one_var in data[0:-1]:
    split_num = int(data.index(one_var))
    var_name = one_var[-1] [0]
    files_amt = one_var[-1][1]
    flag = 1
    accuate = 0
    for i in range(0, files_amt):
        # w*x+b
        judge_func = var_amt - 1
        for j in range(0, var_amt):
            if j == split_num:
                continue
            if (vector_multi(w[split_num], one_var[i], b[split_num]) >= vector_multi(w[j], one_var[i], b[j])):
                # adjust the w and b
                judge_func -= 1
        if judge_func == 0:
            # print("accuate")
            accuate += 1
        # else:
            # print("false")
    # print(accuate)
    print(accuate/files_amt)

















#only for test------------------------------------------------------------------------------------------------------

""" while(1):
    for one_var in data:
        split_num = data.index(one_var)
        var_name = one_var[-1] [0]
        files_amt = one_var[-1][1]
        while(1):
            flag = 1
            for i in range(0, files_amt):
                # w*x+b
                for j in range(0, var_amt):
                    if j == split_num:
                        continue
                    if (vector_multi(w[split_num], one_var[i], b[split_num]) <= vector_multi(w[split_num[j]], one_var[i], b[j])):
                        # adjust the w and b
                        w[split_num] = adjustw(w[split_num], one_var[i], step, 1)
                        w[j] = adjustw(w[j], one_var[i], step, -1)
                        b[split_num] += step
                        b[j] += step
                        flag = 0
            if flag == 1:
                break """

                
            







            
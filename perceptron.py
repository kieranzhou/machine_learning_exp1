# this file is for calculate the perceptron
# step1:read the file from frequency.txt----------------------------------------
import re
import sys
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

def printw(w):
    for i in range(0, len(w) - 1):
        print(w[i])
    
data = []
# empty_list = [] append(copy.deepcopy(empty_list))
counter = 0      #counter is for vars
with open('train_frequency.txt', 'r') as f:
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
print("read the train dataset")                            
#part2: reading the dictionary--------------------------------------------------------------------------------------------------------------------------

stat_dic = []   #need to change the global dic
fp = open('Dictionary.txt', encoding = 'gb18030', errors= 'ignore')
for line in fp.readlines():
    stat_dic.append(line.strip('\n'))
fp.close()
print("read the Dictionary")

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
print("finish estimate the parameters primarily")
# try till it satisfy the result or try serveral times and just have an well result
# step could be deliminate with the loop goes on.
# i thought it is the second option that could just be so-so answer. mix

#only for test------------------------------------------------------------------------------------------------------
strarrs = ['/','|','\\']
times = 20
chartime = times/20
for time in range(0, times):
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
                    vector_the = vector_multi(w[split_num], one_var[i], b[split_num])
                    vector_other = vector_multi(w[j], one_var[i], b[j])
                    if (vector_the <= vector_other):
                        # adjust the w and b
                        w[split_num] = adjustw(w[split_num], one_var[i], step, 1)
                        w[j] = adjustw(w[j], one_var[i], step, -1)
                        b[split_num] += step 
                        b[j] -= step 
                        flag = 0
            if flag == 1:
                break
    # for i in range(0, var_amt):
    #     printw(w[i])
    sys.stdout.write(strarrs[time % 3] + '{}/{}:'.format(time+1, times) + '>' * (int(time/chartime)) + '\r')
    sys.stdout.flush()

# approxmately 100  and maybe we could successed it, but maybe it is too similar with the train data
# adjusting the parameter is the most important affair now.

print("train data check------------------------------------------------------------")
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
    print(var_name + ":" + str(accuate/files_amt))



#only for test------------------------------------------------------------------------------------------------------

# writing the checking function for all the testing data
print("test data check-----------------------------------------------------------------") 

test_data = []
# empty_list = [] append(copy.deepcopy(empty_list))
test_counter = 0      #counter is for vars
with open('test_frequency.txt', 'r') as f:
    alldata = f.readlines()
    for temp_var in alldata:
        tmp_list = list(filter(None, re.split(r'[\s\n]\s*', temp_var)))
        test_data.append([])         #vars
        var_name = tmp_list[0]
        files_amt = int(tmp_list[1])
        temp_point = 2
        for i in range(0, files_amt):
            test_data[test_counter].append([])        #files
            characters_amt = int(tmp_list[temp_point])
            temp_point += 1
            for j in range(0, characters_amt):
                # read 4 element
                four_elements = [int(tmp_list[temp_point]), float(tmp_list[temp_point + 1]), float(tmp_list[temp_point + 2]), float(tmp_list[temp_point + 3])]
                test_data[test_counter][i].append(four_elements)
                temp_point += 4
            test_data[test_counter][i].append(characters_amt) #adding characters amount
        test_data[test_counter].append([var_name, files_amt]) #adding files amount
        test_counter += 1
    test_data.append(test_counter)                            #adding vars amount
print("read the testing dataset")

all_file = 0
all_accuate = 0
for one_var in test_data[0:-1]:
    split_num = int(test_data.index(one_var))
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
            vector_the = vector_multi(w[split_num], one_var[i], b[split_num])
            vector_other = vector_multi(w[j], one_var[i], b[j])
            if (vector_the >= vector_other):
                # adjust the w and b
                judge_func -= 1
            else:
                print("vectorthe:" + str(vector_the))
                print("vectorother:" + str(j) + '\t' + str(vector_other))
        if judge_func == 0:
            # print("accuate")
            accuate += 1
        # else:
            # print("false")
    # print(accuate)
    print(var_name + ":" + str(accuate/files_amt))
    all_accuate += accuate
    all_file += files_amt
print("global accurate rate is " + str(all_accuate/all_file))
            







            
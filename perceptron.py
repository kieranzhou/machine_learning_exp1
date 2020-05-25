# this file is for calculate the perceptron
# step1:read the file from frequency.txt----------------------------------------
import re
import sys
import math
import time
def zerolistmaker(n, k):
    listofzeros = [k] * n
    # print(type(listofzeros))
    return listofzeros

def vector_multi(w, x):
    length = x[-1]
    total = 0
    for i in range(0, length):
        temp = x[i][0]
        total += w[temp] * x[i][3]
    return total

def adjustw(w, x, step, para):
    length = x[-1]
    for i in range (0, length):
        temp = x[i][0]
        w[temp] += step * x[i][3] * para
    return w
  
def checker(test_data, w):
    all_file = 0
    all_accuate = 0
    for one_var in test_data[0:-1]:
        split_num = int(test_data.index(one_var))
        files_amt = one_var[-1][1]
        accuate = 0
        for i in range(0, files_amt):
            # w*x+b
            judge_func = var_amt - 1
            for j in range(0, var_amt):
                if j == split_num:
                    continue
                vector_the = vector_multi(w[split_num], one_var[i])
                vector_other = vector_multi(w[j], one_var[i])
                if (vector_the >= vector_other):
                    # adjust the w and b
                    judge_func -= 1
                # else:
                #     print("vectorthe:" + str(vector_the))
                #     print("vectorother:" + str(j) + '\t' + str(vector_other))
            if judge_func == 0:
                # print("accuate")
                accuate += 1
        #     else:
        #         print("false")
        # print(accuate)
        # print(var_name + ":" + str(accuate/files_amt))
        all_accuate += accuate
        all_file += files_amt
    print("global accurate rate is " + str(all_accuate/all_file))
    return all_accuate/all_file

data = []
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

# step3:read the testfile

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

#part4: preparing for the perceptron--------------------------------------------------------------------------------------------------------------------------

# creating n spliters, preparing the parameters
# the form is f(wx+b), init the w and b
var_amt = data[-1]
w = []
for i in range(0, var_amt):
    w.append(zerolistmaker(len(stat_dic), 0))

# define the learning_step and threshold, preset 0.1 and ?not sure
# try till it satisfy the result or try serveral times and just have an well result
# step could be deliminate with the loop goes on.
# i thought it is the second option that could just be so-so answer. mix

strarrs = ['/','|','\\']
step = 1
times = 50
chartime = times/20
lastcheck = -1
for runtime in range(0, times):
    start_time = time.time()
    for one_var in data[0:-1]:
        split_num = int(data.index(one_var))
        var_name = one_var[-1] [0]
        files_amt = one_var[-1][1]
        temp_counter = 0
        while(1):
            temp_counter += 1
            flag = 1
            for i in range(0, files_amt):
                # w*x+b
                actural_step = step * math.pow(0.95, runtime)
                # actural_step = step
                vector_the = vector_multi(w[split_num], one_var[i])
                for j in range(0, var_amt):
                    if j == split_num:
                        continue
                    vector_other = vector_multi(w[j], one_var[i])
                    if (vector_the <= vector_other and one_var[i][-1] != 0):
                        # adjust the w and b
                        w[split_num] = adjustw(w[split_num], one_var[i], actural_step, 1)
                        w[j] = adjustw(w[j], one_var[i], actural_step, -1)
                        sys.stdout.write(strarrs[temp_counter % 3] + "changing" + '\r')
                        sys.stdout.flush()
                        # b[split_num] += actural_step
                        # b[j] -= actural_step
                        flag = 0
                        # print("file no: " + str(i)+ "\tmaking changes\t" + str(split_num) + '\t' + str(j))
            if flag == 1:
                break
        print("loop:" + str(temp_counter) + "\tvar_name\t" + var_name)
    # for i in range(0, var_amt):
    end_time = time.time()
    # if runtime > 100:
    this_check = checker(test_data, w)
    if lastcheck == this_check:
        break
    lastcheck = this_check
    sys.stdout.write(strarrs[runtime % 3] + '{}/{}:'.format(runtime+1, times) +'speed' + str(end_time - start_time) + '>' * (int(runtime/chartime)) + '\r')
    sys.stdout.flush()
# approxmately 100  and maybe we could successed it, but maybe it is too similar with the train data
# adjusting the parameter is the most important affair now.

checker(test_data, w)

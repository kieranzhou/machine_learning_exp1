# this file is for calculate the perceptron
# step1:read the file from frequency.txt----------------------------------------
import re
def zerolistmaker(n):
    listofzeros = [0] * n
    print(type(listofzeros))
    return listofzeros

def vector_multi(m, n):
    



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
var_amts = data[-1]
w = []
for i in range(0, var_amts):
    w.append(zerolistmaker(len(stat_dic)))
b = zerolistmaker(var_amts)
# define the learning_step and threshold, preset 0.1 and ?not sure
step = 0.01
threshold = 0.5

for one_var in data:
    var_name = one_var[-1] [0]
    files_amt = one_var[-1][1]
    while(1):
        for i in range(0, files_amt):
            # w*x+b
            if 
            







            
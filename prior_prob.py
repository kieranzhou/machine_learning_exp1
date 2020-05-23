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

new_data_structure = []
for var in data[0:-1]:
    var_name = var[-1][0]
    files_amt = var[-1][1]
    var_total_num = 0
    for i in range(0, files_amt):
        attr_amt = var[i][-1]
        file_total_num = 0
        min = 1 
        for j in range(0, attr_amt):
            if var[i][j][1] < min:
                min = var[i][j][1]
                
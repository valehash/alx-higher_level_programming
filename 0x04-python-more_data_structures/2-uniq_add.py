def uniq_add(my_list=[]):
    count = 0
    sum = 0
    uniq_list= []
    for x in my_list:
        if x not in uniq_list:
            uniq_list.append(x)
    length =  len(uniq_list)
    while (count < length):
        sum = sum +uniq_list[count]
        count += 1
    return sum

def romanToInteger(string):
    dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    new_list = []
    counter = 0
    
    string_list = [x for x in string]
    
    i = 0
    
    while i <= len(string_list)-1:
        if i == len(string_list)-1:
            new_list.append(string_list[i])
            break
        if dictionary[string_list[i]] < dictionary[string_list[i+1]]:
            new_list.append(string_list[i]+string_list[i+1])
            i +=2 
        else:
            new_list.append(string_list[i])
            i += 1
    
    new_list1 = []
    new_list2 = []
    
    for x in new_list:
        if len(x)==1:
            new_list1.append(x)
        else:
            new_list2.append(x)
    
    binary_sum = []
    for a in new_list2:
        first_number = dictionary[a[0]]
        second_number = dictionary[a[1]]
        
        binary_sum.append(second_number-first_number)
    second_sum = [dictionary[x] for x in new_list1]
    
    sum1 = sum(binary_sum)
    sum2 = sum(second_sum)
    final_sum = sum1 + sum2

         
    return final_sum
        
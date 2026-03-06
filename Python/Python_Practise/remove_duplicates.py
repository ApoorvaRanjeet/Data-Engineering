def duplicates(data):
    new_list=[]
    for i in data:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(duplicates([1,2,3,3,2,4]))
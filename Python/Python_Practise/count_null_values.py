def count_nulls(data):
    count=0
    for i in data:
        if i is None:
            count+=1
    return count

print(count_nulls([10, None, 5, None, 7]))
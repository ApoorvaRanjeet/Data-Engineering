def second_large(numbers):
    largest=float('-inf')
    second=float('-inf')
    
    for i in numbers:
        if i>largest:
            second=largest
            largest=i
        elif i>second and i!=largest:
            second=i
    return second

print(second_large([1,2,3,4]))
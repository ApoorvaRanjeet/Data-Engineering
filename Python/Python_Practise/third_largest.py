def third_large(numbers):
    largest=float('-inf')
    second=float('-inf')
    third=float('-inf')
    
    for i in numbers:
        if i>largest:
            third=second
            second=largest
            largest=i
        elif i>second and i!=largest:
            third=second
            second=i
        elif i>third and i!=second and i!=largest:
            third=i
    return third

print(third_large([5,5]))
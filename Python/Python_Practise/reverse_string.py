def reverse(text):
    length=len(text)
    new_str=''
    for i in range(0,length):
        new_str=new_str+text[length-i-1]
        
    return new_str

print(reverse("sonu"))

# t='abc'
# length=len(t)
# for i in range(0,length):
#     print(length-i-1)
    
print('IMported my module....')

test="hello"
def find_index(text,target):
    for i,value in enumerate(text):   # enumerate helps to keep the track of index and value of each element
        if value==target:
            return i
    return -1

        
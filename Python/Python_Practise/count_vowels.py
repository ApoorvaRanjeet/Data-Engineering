def count_vowels(text):
    count=0
    for c in text:
        c=c.lower()
        if  c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
            count+=1
    return count

print(count_vowels("APOORVA"))
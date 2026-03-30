def occuranece(str1, str2):
    
    alphabet="abcdefghijklmnopqrstuvwxyz"
    occurance=[0]*26


    for c in str1:
        if c in alphabet:
            occurance[alphabet.index(c)]+=1

    for c in str2:
        if c in alphabet:
            occurance[alphabet.index(c)]-=1

    for i in occurance:
        if i !=0:
            return False

    return True     


print(occuranece(" habc4c", "c,cbha "))
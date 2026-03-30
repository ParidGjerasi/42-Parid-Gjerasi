def rotate_one(word: str, index: int):
    alphabet="abcdefghijklmnopkrstuvwxyz"
    index=index%26
    result=""

    for c in fjala:
        if c in alphabet:
            if alphabet.index(c)<26-index:
                c=alphabet[alphabet.index(c)+index]
            else:
                c=alphabet[alphabet.index(c)-(26-index)]
        result+=c
    return result


print(rotate_one("az", 5))
print(rotate_one("az", 2))
print(rotate_one("az", 67))
print(rotate_one("az", 90))
print(rotate_one("az", 2))
print(rotate_one("az", 1))
print(rotate_one("az", 7))



alphabet=""
index=index%26

for c in word:
    if c in alphabet:
    if alphabet.index(c)<26-index


# no prototpye for this yet

#built in version idk if test allows
x = 'Hello'
x_length = len(x)
print(x_length) 

#manual version similar to C logic
def strlen(string) -> int:
    i = 0
    for index in string:
        i = i+1
    return i
def main():
    print (strlen("Hello"))
main()
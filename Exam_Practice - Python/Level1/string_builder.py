# string_builder and it required to alterate the string from lowercase to uppercase character by character


name = "BERTI" #ifykyk ;))

def string(name:str)-> str:
    result = []
    for char in name:
        if char.islower():
         char= char.upper()
        elif char.isupper():
            char = char.lower()
        result.append(char)
    return "" .join(result)

print(string(name))
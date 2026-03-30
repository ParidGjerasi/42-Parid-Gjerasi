

# ke nje string with numbers find pares 1234abc56   
      
def sequence(fjala:str):

    numbers="0123456789"
    pares=0

    for i in range(len(fjala)-1):
        if fjala[i] in numbers and fjala[i+1] in numbers:
            if int(fjala[i])==int(fjala[i+1])-1:
                pares+=1
    

    return pares

print(sequence("1234abc56"))
             
    
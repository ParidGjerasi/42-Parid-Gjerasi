word = "Ana" # no need to put it in the exam just for testing 
def is_palindrome(word: str) -> bool:
    lowerword= word.lower() #case sensitive checker
    return lowerword == lowerword[::-1]
print(is_palindrome(word)) # returns true if u do Berti return False 
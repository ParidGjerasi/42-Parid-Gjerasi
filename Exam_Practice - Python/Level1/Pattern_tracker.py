# prototpye: Pattern Tracker

# Allowed functions: None

# Write a function that counts the number of valid consecutive digit pairs in a string.
# A valid pair consists of two adjacent digits where the second digit is exactly one greater than the first digit.
# A 9 followed by a 0 is not a valid pair and only consider consecutive characters that are both digits (0-9).

# def pattern_tracker(text: str) -> int:
# Input:  pattern_tracker("123")
# Output: 2

# Input:  pattern_tracker("12034")
# Output: 2

# Input:  pattern_tracker("987654321")
# Output: 0

# Input:  pattern_tracker("01234567")
# Output: 7

# SUCCESFULL

def pattern_tracker(text: str) -> int:

    numbers = ['0','1','2','3','4','5','6','7','8','9']
    digits = [0,1,2,3,4,5,6,7,8,9]

    valid_numbers_list = []
    counter = 0

    for i in text:
        if i in numbers:
            i = int(i)
            valid_numbers_list.append(i)
        else:
            valid_numbers_list.append(i)

    j = 0
    k = j + 1

    while j < (len(valid_numbers_list) - 1):
        while k < len(valid_numbers_list):
            if valid_numbers_list[k] in digits and valid_numbers_list[j] in digits:
                if valid_numbers_list[k] - valid_numbers_list[j] == 1:
                    counter += 1

            k += 1
            j += 1

        j += 1

    return counter

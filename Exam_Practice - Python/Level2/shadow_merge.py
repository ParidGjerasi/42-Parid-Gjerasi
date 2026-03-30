# PROTOTYPE Shadow Merge

# Allowed functions: None

# Write a function that merges two sorted lists into one sorted list.

# def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

# Input:  shadow_merge([1,3,5], [2,4,6])
# Output: [1,2,3,4,5,6]

# Input:  shadow_merge([1,2,3], [4,5,6])
# Output: [1,2,3,4,5,6]

# Input:  shadow_merge([1], [2,3,4])
# Output: [1,2,3,4]

# Input:  shadow_merge([], [1,2,3,4])
# Output: [1,2,3,4]

# Input:  shadow_merge([1,1,2], [1,3,3])
# Output: [1,1,2,3]

# SUCCESSFUL

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:

    merged = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

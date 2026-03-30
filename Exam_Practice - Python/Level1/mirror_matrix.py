#Reverse the rows for each of them or vertical reverse

food = ["banana", "apple", "strawberry"]
sweets = ["snickers", "ice cream", "jello"]
drinks = ["pepsi", "sprite", "orange juice"]

fridge = food, sweets, drinks

def mirror_matrix(matrix: list) -> None:

    print (matrix[::-1]) #verticall movement
mirror_matrix(fridge)


def mirror_matrix(matrix: list) -> None:

    for  items in matrix:
        items[::-1] #horizontal movement
mirror_matrix(fridge)
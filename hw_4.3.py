def algorithm(stairs):
    if stairs == 0:
        return 1
    if stairs < 0:
        return 0
    return algorithm(stairs - 1) + algorithm(stairs - 2)

print("Please, enter number of stairs")
number_of_stairs = int(input())
print("It is count of all ways:", algorithm(number_of_stairs))
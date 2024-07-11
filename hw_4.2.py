def euclid_algorithm(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_1 == num_2:
        return num_1
    if num_1 > num_2:
        return euclid_algorithm(num_1 - num_2, num_2)
    return euclid_algorithm(num_1, num_2 - num_1)


print("Plese, enter two numbres")
a, b = map(int, input().split(" "))

print("It is their greatest common divisor:", euclid_algorithm(a, b))
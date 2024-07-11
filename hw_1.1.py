n = int(input())

for level_index in range(n):
    print(" " * (((n * 2 - 1) - ((level_index + 1) * 2 - 1)) // 2), "*" * ((level_index + 1) * 2 - 1), " " * (((n * 2 - 1) - ((level_index + 1) * 2 - 1)) // 2), sep="")
try:
    input_file = open('cities.txt', 'r')
    output_file = open('filtered_cities.txt', 'w')

    print("Enter minimal popultion")
    minimal_population = int(input())

    list_of_names = []
    for string in input_file.readlines():
        name_of_city, population = string.split(":")
        if int(population) > minimal_population:
            list_of_names.append(name_of_city)
    list_of_names.sort()
    output_file.write("\n".join(list_of_names))
    input_file.close()
    output_file.close()
except FileNotFoundError:
    print("Error! Some file not found!")
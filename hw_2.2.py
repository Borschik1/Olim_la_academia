try:
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')

    print("Enter sumbols for deleting")
    symbols_black_list = input()

    for string in input_file.readlines():
        if string[-1] == "\n":
            string = string[:-1]
        while string[-1] in symbols_black_list:
            string = string[:-1]
        string += ";"
        string = string[::-1] + "\n"
        output_file.write(string)

except FileNotFoundError:
    print("Error! Some file not found!")
    exit(0)
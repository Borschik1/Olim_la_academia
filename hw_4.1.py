try:
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')

    stack = []
    symbol = input_file.read(1)
    while symbol != "":
        if symbol not in "()<>[]{}":
            symbol = input_file.read(1)
            continue
        if symbol in "<{[(":
            stack.append(symbol)
        else:
            try:
                stack_symbol = stack.pop()

                if stack_symbol + symbol not in ["{}", "[]", "<>", "()"]:
                    output_file.write("false")
                    input_file.close()
                    output_file.close()
                    exit(0)
            except IndexError:
                output_file.write("false")
                input_file.close()
                output_file.close()
                exit(0)
        symbol = input_file.read(1)

    if stack:
        output_file.write("false")
    else:
        output_file.write("true")

    input_file.close()
    output_file.close()
except FileNotFoundError:
    print("Error! Some file not found!")
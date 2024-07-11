try:
    input_file = open('input.txt', 'r')
    output_file = open('output.txt', 'w')

    final_string = ""
    total_marks = 0
    pairs = input_file.readlines()
    if not pairs:
        print("Error! Empty input-file")
        input_file.close()
        output_file.close()
        exit(0)
    for pair in pairs:
        name_and_mark = pair.split(",")
        if len(name_and_mark) != 2:
            print("Error! Wrong data structure")
            input_file.close()
            output_file.close()
            exit(0)
        try:
            total_marks += int(name_and_mark[1])
        except ValueError:
            print("Error! Wrong data structure")
            input_file.close()
            output_file.close()
            exit(0)

    average_mark = total_marks / len(pairs)

    for pair in pairs:
        name, mark = pair.split(",")
        if int(mark) > average_mark:
            final_string += name + "\n"

    output_file.write(final_string)

    input_file.close()
    output_file.close()
except FileNotFoundError:
    print("Error! Some file not found!")
    exit(0)
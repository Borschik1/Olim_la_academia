try:
    input1_file = open('input1.txt', 'r')
    input2_file = open('input2.txt', 'r')
    output_file = open('output.txt', 'w')

    final_string = input1_file.read() + input2_file.read()
    output_file.write("".join(sorted(final_string)))

    input1_file.close()
    input2_file.close()
    output_file.close()
except FileNotFoundError:
    print("Error! Some file not found!")
    exit(0)
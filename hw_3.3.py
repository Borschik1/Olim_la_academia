import re

try:
    input_file = open('input.txt', 'r')

    dict_of_courses = {}
    line = input_file.readline()

    while line:
        #print(line)
        text_of_line = re.split("[,.:\\s]+", line)
        name = text_of_line[0]
        for word_indx in range(1, len(text_of_line)):
            if not text_of_line[word_indx]:
                continue
            if text_of_line[word_indx] not in dict_of_courses.keys():
                dict_of_courses[text_of_line[word_indx]] = [name]
            else:
                dict_of_courses[text_of_line[word_indx]].append(name)

        line = input_file.readline()


    print("Please, enter name of the course.")
    name_of_course = input()
    print("There are all signed up students: ", " ,".join(dict_of_courses[name_of_course]), sep="")

    input_file.close()
except FileNotFoundError:
    print("Error! Some file not found!")
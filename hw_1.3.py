def operation(number):
    if len(number) == 1:
        return int(number)
    answer = 0
    for sub_number in number:
        answer += int(sub_number)
    return operation(str(answer))


number = input()
print(operation(number))
number = input()

hundreds = False
tens = False
ones = False

if len(number) == 3:
    hundreds = number[0]
    tens = number[1]
    ones = number[2]
elif len(number) == 2:
    tens = number[0]
    ones = number[1]
else:
    ones = number[0]
#print(hundreds, tens, ones)

if hundreds:
    match hundreds:
        case "1":
            print("сто", end=" ")
        case "2":
            print("двести", end=" ")
        case "3":
            print("триста", end=" ")
        case "4":
            print("четыреста", end=" ")
        case "5":
            print("пятьсот", end=" ")
        case "6":
            print("шестьсот", end=" ")
        case "7":
            print("семьсот", end=" ")
        case "8":
            print("восемьсот", end=" ")
        case "9":
            print("девятьсот", end=" ")

if tens:
    match tens:
        case "1":
            match ones:
                case "1":
                    print("одиннадцать", end=" ")
                case "2":
                    print("двенадцать", end=" ")
                case "3":
                    print("тринадцать", end=" ")
                case "4":
                    print("четырнадцать", end=" ")
                case "5":
                    print("пятнадцать", end=" ")
                case "6":
                    print("шестнадцать", end=" ")
                case "7":
                    print("семнадцать", end=" ")
                case "8":
                    print("восемнадцать", end=" ")
                case "9":
                    print("девятнадцать", end=" ")
                case "0":
                    print("десять")
            exit(0)
        case "2":
            print("двадцать", end=" ")
        case "3":
            print("тридцать", end=" ")
        case "4":
            print("сорок", end=" ")
        case "5":
            print("пятьдесят", end=" ")
        case "6":
            print("шестьдесят", end=" ")
        case "7":
            print("семьдесят", end=" ")
        case "8":
            print("восемьдесят", end=" ")
        case "9":
            print("девяносто", end=" ")

match ones:
    case "1":
        print("один")
    case "2":
        print("два")
    case "3":
        print("три")
    case "4":
        print("четыре")
    case "5":
        print("пять")
    case "6":
        print("шесть")
    case "7":
        print("семь")
    case "8":
        print("восемь")
    case "9":
        print("девять")
    case "0":
        print("")
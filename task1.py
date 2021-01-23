import sys


def salary():
    arg_1, arg_2, arg_3 = sys.argv[1:]
    result = int(arg_1)*int(arg_2)+int(arg_3)
    print(result)
    return result

salary()
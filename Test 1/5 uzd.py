import collections


x = "aaavvvfdff"


def Func(x):
    previous_char = ''
    new_x = ''
    count = 0
    for char in x:
        if char == previous_char:
            count += 1
            print(count)
        elif char != previous_char and previous_char != '':
            new_x += char + str(count)
            count = 0
            previous_char = char
        else:
            new_x += char
            previous_char = char
    print(new_x)


Func(x)

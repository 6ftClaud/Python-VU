data_list = [
    [1, 10, 34, 110, 400, 30, 20],
    [-5, -10, 55, 120, 30],
    [2, 67, 23, 78, 200],
]
"""
data_list = [
    [-1, 45, 23, 32, 999],
    [67, 99, 23],
    [23],
]
"""


def Calc(a):
    # Defining variables
    max_value = 0
    min_value = 0
    sum_value = 0
    average = 0

    # Filtering the list
    a = [i for i in a if i >= 10 and i < 100]

    # Calculating values with pre-defined Python functions
    max_value = max(a)
    min_value = min(a)
    sum_value = sum(a)
    average = (sum_value / len(a))

    # Returning tuple of values
    return (average, min_value, max_value, sum_value)


def Calc_List(b):
    # For list in b call Calc function
    for data_list in b:
        print(Calc(data_list))


print("Average/Min/Max/Sum")
Calc_List(data_list)

"""
n = "vienas du trys"
a = "vn "
b = "ayds"
"""
n = "keturiolika"
a = "ktur"
b = "ila"


def Char_To_Int(n, a, b):
    # Creates an array of characters that are in a and b strings
    ab_chars = [char for char in (a + b)]
    # Variable to store new n value that doesnt contain characters in ab_chars
    new_n = ''
    # Variable to store the result
    total = 0

    # For each character in a, add 1 to total
    for char in a:
        total += 1

    # For each character in b, remove 1 from total
    for char in b:
        total -= 1

    # Iterate over characters in n to find out if they're in ab_chars
    # If they're not, add character to new string
    # This is not needed, because their value is 0 anyway and the result wouldn't change
    for char in n:
        if char not in ab_chars:
            new_n += char
    # print(new_n)

    # Return total value
    return total


total = Char_To_Int(n, a, b)
print(total)

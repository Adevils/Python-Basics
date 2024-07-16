def binary_numb(inp):

    change=str(inp)

    for char in change:
        if char not in("0","1"):
            return "Not a binary number"
    return "Binary number"

val=9001
print(binary_numb(val))            
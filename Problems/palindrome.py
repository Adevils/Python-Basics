def palindrome_num(inp):

    change=str(inp)

    for i in change:

        if change == change[::-1]:
            return f"{inp} is a palindrome number"

        else:
            return f"{inp} is not a palindrome number"   

val=123
print(palindrome_num(val))            
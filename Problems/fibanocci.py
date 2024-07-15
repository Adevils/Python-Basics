def fiba(inp):

    fib=[0,1]

    for i in range(2,inp):

        fib.append(fib[-1]+fib[-2])

    return fib

num = 1
print(fiba(num))

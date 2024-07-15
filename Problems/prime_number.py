def primeornot(inp):

    
    for i in range(2,(inp//2)+1):
        if inp%i ==0:
            
            return f"the{inp} is not prime"
            
    return f"the {inp} is prime"

val=6
print(primeornot(val))
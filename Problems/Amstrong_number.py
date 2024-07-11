"newlist = [expression for item in iterable if condition == True]"

def amstrong_num (inp):


    length=len(inp) 
    final=sum(int(digit)**length for digit in inp)
      

    return final  


val="153"
sol=amstrong_num(val)

if int(val)==sol:
    print(f"{sol} is a amstrong number")

else:
    print("No amstrong number")  
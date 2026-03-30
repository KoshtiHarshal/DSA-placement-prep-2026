def power_of_three(n):
    if n<=0:
        return False
    elif n==1:
        return True
    elif n%3!=0:
        return False
    else:
        return True
        
n= int(input("Enter a number: "))
print(power_of_three(n))
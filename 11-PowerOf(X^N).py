def power_of_x_n(x, n):
    if n == 0:
        return 1
    elif n<0:
        return 1 / power_of_x_n(x, -n)
    elif n % 2 == 0:
        a = power_of_x_n(x, n // 2)
        return a * a
    else:
        return x * power_of_x_n(x, n - 1)
    
n= int(input("Enter the value of n: "))
x= int(input("Enter the value of x: "))
print("The value of", x, "to the power of", n, "is", power_of_x_n(x, n))
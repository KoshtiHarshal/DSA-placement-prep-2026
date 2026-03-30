#Count Odd numbers in an interval of range.
def count_odd_numbers(a,b):
    count=0
    for i in range(a,b+1):
        if i%2!=0:
            count+=1
    return count
a=int(input("Enter the starting number: "))
b=int(input("Enter the ending number: "))
result=count_odd_numbers(a,b)
print("The count of odd numbers between",a,"and",b,"is:",result)

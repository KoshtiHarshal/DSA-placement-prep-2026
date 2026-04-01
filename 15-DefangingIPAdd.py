# Defang an IP address, which means to replace every period "." with "[.]".


IP_Add = str(input("Enter the first IP address: "))
# Method 1: Using the replace() method to defang the IP address.
def defangIPaddr(IP_Add):
    return IP_Add.replace(".", "[.]")

print(defangIPaddr(IP_Add))

# Method 2: Using a loop to iterate through each character in the IP address and construct the defanged IP address.
NewIP_Add = ""
for i in IP_Add:
    if i == ".":
        NewIP_Add += "[.]"
    else:
        NewIP_Add += i
print("The defanged IP address is:", NewIP_Add)
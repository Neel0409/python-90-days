# User se birth year lo aur 2026 mein approximate age calculate karo.

birth_year = int(input("Enter Your Birth Year "))

age = 2026 - birth_year

print("Your Age is : ",age)


# User se length aur width lo aur rectangle ka area print karo.

length = float(input("Enter a lenghth :"))

width = float(input("Enter a width"))

area = length * width 

print("Area is ",area)

#Celsius temperature input lo aur Fahrenheit mein convert karo.
#f = (c * 9/5) + 32

c = float(input("Enter a celsius temperature :"))

f =(c * 9/5) + 32 

# Do variables ki values third variable ki help se swap karo

var1 = 31
var2 = 60

temp = var1
var1 = var2
var2 = temp 

print(var1)
print(var2)

# Teen items ki prices input lo aur total bill calculate karo.

item1 = int(input("Enter a value1 :"))
item2 = int(input("Enter a value2 :"))
item3 = int(input("Enter a value3 :"))

total_bill = item1 + item2 + item3 

print("Your Bill is ",total_bill)
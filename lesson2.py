'''
Name: Abe Weber
Date: 9/24/24
Description: More on f-strings,input, and numbers/ops
'''

my_int = 5
my_float = 6.38
print(f"{my_int} {my_float}")

another_float = 8.0 #make this a float
float_two = float (8) #make a float by casting
print(f"{another_float} {float_two}")

#get decimal from a user
#radius = float(input("Enter a radius:"))
#print(f"You entered a radius of {radius}")

# operations on numbers
# P E MModD AS
# modulus operator or remainder operator
print(15 % 7) # prints the remainder when 15 is divided by 7
print((2+3)*4) # 2+3 first, times 4

#exponent is not ^, it is **
print(5**4)# this is 5 to the 4th

#weird math stuff
print(0.3-0.2) # roundoff error - watch out for it

# rounding
# method 1, use round()
num = 3.1415
print(round(num,2))
#method 2, use f string
print(f"{num:.2f}")

#your turn to code
#Ask a user for some amount of US dollars
# Store this in a variable
# Convert that money to some currency of your choice
# store the conversion factor in a variable
# store the final amount in a variable
# print it like this "___ USD is the same as ___

USD = float(input("How many USD do you want to convert"))
Euro = USD*.9
print(f"{USD} is equal to {Euro}")



import math
# Question - 1
# base = float(input("Enter the side of the triangle: "))
# height = float(input("Enter the side of the triangle: "))

# # base = 10
# # height = 10

# area_of_triangle = 1/2*base*height

# print(f"Area of triangle is {area_of_triangle}")

# question - 2
# celsius = float(input("Enter temperature in celcuius"))

# # converting celsius to farenhite

# farenhite = (celsius * 9/5) + 32

# print(f"{celsius} C into {farenhite} F")

# question - 3
# radius = 10 # for test purpose
# radius = float(input("Enter the value of radius"))

# area = math.pi*(radius**2)
# circumference = 2*math.pi*radius

# print(f"The circumference of circle is : {circumference:.2f} and area is {area:.2f}")

# question - 4

# def checkPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if(num % i == 0):
#             return False       
#     return True

# num = 10
# if checkPrime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# question - 5
# num = [1,2,3,4,5,6,7,8,9,10]
# i = 0
# avg = 0
# while i < len(num):
#     avg += num[i]
#     i+=1

# print(f"Average of number is {avg/len(num)}")

# num = [1,2,3,4,5,6,7,8,9,10]

# print(num[::-1])



# question - 7
digit = 123
sum = 0
while digit > 0:
    sum += digit%10
    digit = digit//10

print(f"sum: {sum}")


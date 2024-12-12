#i)
def circle_area():
    radius = int(input("Enter the raduis of the circle:\n"))
    pie=float(3.14)
    area=pie*radius**2
    print(f"The radious of the circle with {radius} radious is {area} ")
circle_area()
  

# #ii)
numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for num in numbers:
    if num % 2 != 0:
        print(num)
        odd_sum += num
print("Sum of odd numbers:", odd_sum)

# #iii)

def numbers():
    number_1 = int(input("Enter the first number :"))
    number_2 =int(input("Enter the second number"))

    the_sum = number_1+number_2
    print(f"The sum of the numbers is {the_sum}")

    the_difference = number_1-number_2
    print(f"The difference of the numbers is {the_difference}")

    the_product = number_1*number_2
    print(f"The product of the numbers is {the_product}")

    the_quotient = number_1/number_2
    print(f"The quotient of the numbers is {the_quotient}")
numbers()


#iv)
dictionary = {
   "name" : "Alice",
   "age" : 20,
   "grade" :"A"

}
print(dictionary)

dictionary["age"] = 26
print(dictionary)

dictionary['city'] = 'kampala'
print(dictionary)
# #i)
student_name = input('Enter the student name : ')
student_number = input('enter the student number : ')
programming = int(input("Enter the programming marks : "))
data_science = int(input("Enter the Data science marks : "))
computer_applications = int(input("Enter the computer applications marks : "))


total_marks = programming+data_science+computer_applications
print(total_marks)

total_number_of_subjects = 3

average_mark = total_marks/total_number_of_subjects

print(f"The students average mark is : {average_mark:.3f}")

#ii)
miles_driven = int(input("Enter the miles driven : "))

gallons_used = int(input("Enter the gallons used : "))

miles_per_gallons = miles_driven/gallons_used

print(f"The cars miles per gallons used is {miles_per_gallons}")

#iii)
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,
        27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,
        51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70, 71,72,73,74,
        75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101]
for numbers in range(1, 101):
    if numbers % 2 != 0:
        print(numbers)

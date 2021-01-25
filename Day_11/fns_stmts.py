# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print('\n')
print('Solution for Question 01')
def sum_2(num1, num2):
    sum_2numbers = num1+num2
    print(sum_2numbers)
sum_2(5,15)
sum_2(15.2, 10)


print('\n')
print('Solution for Question 02')
#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_circle(r):
    pi = 3.14
    area = pi * r**2
    return area
print(area_circle(10))


print('\n')
print('Solution for Question 03')
#Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    total = 0
    for i in nums:
        total += i
    return total
print(add_all_nums(10,20,50,85,25))
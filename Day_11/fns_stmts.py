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

print('\n')
print('Solution for Question 04')
#Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celcius_to-fahrenheit.
def temp_c_to_f(c_temp):
    temp_in_fahrenheit = (c_temp * (9/5)) + 32
    print(f'The Temperature in Fahrenheit is : {temp_in_fahrenheit} F')
temp_c_to_f(27)


print('\n')
print('Solution for Question 05')
#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def season(month):
     if ((month == 'September') or (month =='October')or (month == 'November')):
        print('The season is Autumn')
     elif (month == 'December') or (month =='January') or (month =='February'):
         print('The season is Winter')
     elif (month == 'March') or(month == 'April') or (month =='May'):
        print('The season is Spring')
     elif (month == 'June') or (month =='July') or (month =='August'):
        print('The season is Summer')
season('March')



print('\n')
print('Solution for Question 06')
#Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
l = [12,25,'nipah','Republic',10.9, False]

def print_list(x):
    for i in range(0, len(x)):
        print (x[i])

print_list(l)


print('\n')
print('Solution for Question 07')
#Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(x):
    print(x[::-1])
reverse_list(l)

m = ['fun','nano','tata']
print('\n')
print('Solution for Question 08')
#Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_item(x):
    lst= [n.upper() for n in x]
    print(lst)
capitalize_list_item(m)


print('\n')
print('Solution for Question 09')
#Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(lst, new_item):
    lst.append(new_item)
    print(lst)

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
add_item(food_staff, 'Meat')

numbers = [2, 3, 7, 9]
add_item(numbers, 5)


print('\n')
print('Solution for Question 10')
#Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item_tobe_remove):
    lst.remove(item_tobe_remove)
    print(lst)

remove_item(food_staff, 'Mango')

remove_item(numbers, 3)


print('\n')
print('Solution for Question 11')
#Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(x):
    sum = 0
    for n in range(0, x+1):
        sum = n + sum
    print(sum)
sum_of_numbers(5)
sum_of_numbers(10)
sum_of_numbers(100)

print('\n')
print('Solution for Question 12')
#Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(x):
    sum_odd = 0
    for n in range(0, x+1):
        if (n % 2) != 0:
            sum_odd +=  n
    print(sum_odd)

sum_of_odds(5)                  
sum_of_odds(10)                  
sum_of_odds(100)                  



print('\n')
print('Solution for Question 13')
#Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(x):
    sum_even = 0
    for n in range (0, x+1):
        if (n%2 == 0):
            sum_even += n
    print(sum_even)

sum_of_even(5) 
sum_of_even(15) 
sum_of_even(100) 


print('\n')
print('Solution for Question 14')
#Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(x):
    num_of_odds = 0
    num_of_evens = 0
    for n in range(0, x+1):
        if (n%2 ==0):
            num_of_evens += 1
        else:
            num_of_odds += 1
    print(num_of_evens)
    print(num_of_odds)

evens_and_odds(5)
evens_and_odds(500)


print('\n')
print('Solution for Question 15')
#Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def facto(x):
    fact = 1
    for n in range(1,x+1):
        fact = fact * n
    print(fact)

facto(5) 
facto(10)


print('\n')
print('Solution for Question 16')
#Write a function called is_prime, which checks if a number is prime.

def is_prime(x):
    if x > 1:
        for n in range (2, x):
            if (x % n) == 0: 
                print(f'{x} is not a prime number')
                break
        else:
            print(f'{x} is a prime number')
is_prime(2)
is_prime(3)
is_prime(8)
is_prime(5)
is_prime(110)


print('\n')
print('Solution for Question 17')
#Write a function called print_prime, which prints all primes below a given number.

def print_prime(p):
    for num in range(0, p+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(f'{num} is a prime')

print_prime(100)
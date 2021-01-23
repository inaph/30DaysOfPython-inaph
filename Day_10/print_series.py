#Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
while count < 11:
    print(count)
    count = count + 1

print('#####Question 2')
#Iterate 10 to 0 using for loop, do the same using while loop.
count2 = 10
while count2 >-1:
    print(count2)
    count2 = count2 - 1

print('#####Question 3')
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for number in range(0,8):
    print(number * '#')

print('#####Question 4')
#Use nested loops to create the following:
for number2 in range(0,8):
    if number2 <8:
        print('# ' * 7)


print('#####Question 5')
for number3 in range(0,11):
    if number3 < 11:
        print(f'{number3} * {number3} = {number3 * number3} ')

print("Question6")    
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in lst:
    print(item)

print("  ")
print("Question7")
#Use for loop to iterate from 0 to 100 and print only even numbers
for numbez in range(0,100):
    if ((numbez % 2) == 0):
        print(numbez)
    


print("  ")
print("Question8")
#Use for loop to iterate from 0 to 100 and print only odd numbers
for numbez in range(0,100):
    if ((numbez % 2) != 0):
        print(numbez)


print("  ")
print("Question9")
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum1=0
for number in range(0,101):
    if number <101:
        sum1 = sum1 + number
        number = number + 1
        print(sum1)

print("  ")
print("Question10-a")
#Use for loop to iterate from 0 to 100 and print the sum of all evens.
sum1 = 0
for number in range(0,101):
    if ((number %2) == 0) and (number < 101):
        sum1 = sum1+number
        number = number+1
        print(sum1)

print("  ")
print("Question10-b")
#Use for loop to iterate from 0 to 100 and print the sum of all odds.
sum1 = 0
for number in range(0,101):
    if ((number %2) != 0) and (number < 101):
        sum1 = sum1+number
        number = number+1
        print(sum1)

print("  ")
print("Question11")
#Loop through the countries and extract all the countries containing the word land.
country_lst = ['India','USA','Netherland', 'Japan','Switzerland', 'Finland', 'Greenland']
subs = 'land'
for country in country_lst:
    if subs in country:
        print(country)

print("  ")
print("Question12")
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.

fr_list = ['banana', 'orange', 'mango', 'lemon'] 
for fruit in reversed(fr_list):
    print(fruit)
    

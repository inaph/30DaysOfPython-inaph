"""If a fruit doesn't exist in the list add the fruit to the list and print the
 modified list. If the fruit exists print('That fruit already exist in the list')"""
 
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit= input("Please enter the name of the fruit ")
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
print(fruits)

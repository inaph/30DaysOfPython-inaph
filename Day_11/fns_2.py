
print('\n')
print('Solution for Question 18')
#Write a functions which checks if all items are unique in the list.
lst_1 = [10,20,30,100]

def unique_list(x):
    st_1= set(x)
    if len(x) == len(st_1):
        print('List have Unique items')
    else:
        print("List doesn't have unique items" )

unique_list(lst_1)
print(type(lst_1[0]))

print('\n')
print('Solution for Question 19')
#Write a function which checks if all the items of the list are same data type

def check_d_type(x):
    for item in x:
        if not isinstance(item, type(x[0])):
            break
        else:
            print('False')

check_d_type([10,20,'f'])


print('\n')
print('Solution for Question 20')
#Write a function which check if provided variable is a valid python variable

def valid_py_var(x):
    if type(x) == str:
        print('It is string')
    elif type(x) == int:
        print('It is Interger')
    elif type(x) == bool:
        print("It is Boolean")
    elif type(x) == float:
        print('It is Float')
    else:
        print('NOt a valid data type in python')

valid_py_var(10)
valid_py_var('Phani')
valid_py_var(3.14)
valid_py_var(False)
valid_py_var(2)


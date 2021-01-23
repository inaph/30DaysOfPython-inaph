my_age = 29
your_age = int(input('Enter your age: '))
if my_age > your_age: 
    if (my_age - your_age) >= 2:
        print(f'You are {my_age - your_age} years yourger than me')
    else:
        print(f'You are {my_age - your_age} year yourger than me')
elif my_age == your_age:
    print("We both are of same age")
elif my_age < your_age:
    if (your_age - my_age) >=2:
        print(f'I am {your_age - my_age} years younger than you')
    else:
        print(f'I am {your_age - my_age} year younger than you')

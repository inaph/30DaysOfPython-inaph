a = 'Thirty'
b = 'Days'
c = 'Of'
d = 'Python'
print(a+ ' ' + b+ ' '+c+ ' ' +d)

e = 'Coding ' 
f = 'For '
g = 'All'
company = e+f+g
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.swapcase())
print(company[0:6])
print(company.index('For'))
print(company.find('For'))
print(company.replace('Coding', 'Python'))
com = ("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon")
print(com.split(','))
print(company[0])
print(company[-1])
words1 = "Python FOr Everyone"
acronym1 = ''.join(word[0] for word in words1.upper().split())
print(acronym1)
words2 = "Coding For All people"
acronym2 = ''.join(word[0] for word in words2.upper().split())
print(acronym2)
print(words2.rfind('l'))
words3 = "You cannot end a sentence with because because because is a conjunction"
print(words3.index('because'))
print(words3.find('because'))
print(words3.rindex('because'))
print(words3.rfind('because'))
print(words3[31:54])
print(words3.find('because'))
words4 = "   Coding For All      "
print(len(words4))
print(len(words4.replace('  ', '')))
words5 = '30DaysOfPython'
print(words5.isidentifier())
words6 ='thirty_days_of_python'
print(words6.isidentifier())
words7 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = ' #'.join(words7)
print(result)
words8 = "I am enjoying this challenge. \nI just wonder what is next."
print(words8)
words9 = "Name \tAge \tCountry \nPhani \t29 \tIndia"
print(words9)
radius = 10
area = 3.14 * radius ** 2
print('The area of Circle with radius %d is %.2f meters square' %(radius, area))
print('The area of Circle with radius {} is {} meters square'.format(radius, area))
print(f'The area of Circle with radius {radius} is {area} meters square')
x = 8
y = 6
print(f'{x} + {y} = {x+y}')
print(f'{x} - {y} = {x-y}')
print(f'{x} * {y} = {x*y}')
print(f'{x} / {y} = {x/y}')
print(f'{x} % {y} = {x%y}')
print(f"{x} //{y} = {x//y}")
print(f'{x} ** {y} = {x**y}')
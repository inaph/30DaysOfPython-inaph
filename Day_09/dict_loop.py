person = {
         'first_name': 'Asabeneh',
         'last_name': 'Yetayeh',
         'age': 250,
         'country': 'Finland',
         'is_marred': True,
         'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
         'address': {
                    'street': 'Space street',
                    'zipcode': '02210'
                    }
         }
""" 
1 Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
2 Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
3 If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
4 If the person is married and if he lives in Finland, print the information in the following format:
"""

# to print all skills of person
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
#or #1 can  be written as
for skill in person['skills']:
        print(skill)


#2
for skill in  person['skills']:
        if skill == 'Python':
                print('Yes, Python is present')

#3
while skill in  person['skills']:
        if (skill == 'JavaScript') and (skill == 'React'):
                print('Front End')
      

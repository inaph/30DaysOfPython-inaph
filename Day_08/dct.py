dog = {} #empty dog dictionary
print(dog)
dog = {'name': 'frooty', 
       'color': 'white',
       'breed': 'pamerian',
       'legs': 'medium',
       'age': 7
       }
print(dog)
student = { 'first_name':'Phani',
            'last_name':'Naga',
            'gender':'M',
            'marital_status': 'single',
            'skills':['python','ruby','sql','excel'],
            'country': 'India',
            'city': 'Tenali',
            'addres': {'street': 'BB street',
                        'Dno': '6-72',
                        'pincode': '522211'
                        }
            }
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('java') #add java to skills
student['skills'].append('IBM Db2') #add ibmdb2 to skills
print(student['skills'])
print(student.keys()) #prints keys of dct student
print(student.values()) #prints values of dct student
print(len(student.values())) #prints length of values of dct student
print(type(student.values())) #prints type of values of dct student
print(student.items())
student.pop('city')
print(student.get('city')) #gets item
print('city' in student) #gets bool 
del dog
print(dog)

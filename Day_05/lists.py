emlst = []
print(emlst)
list_5 = ['apple', 'bat', 'car', 'dog', 'eagle']
print(list_5)
print(len(list_5))
print(list_5[0:5:2])
list_mix = ['Phani', 29, 169, 'single', 'Guntur']
print(list_mix)
it_companies = ['Facebook', 'Google','Microsoft','Apple','IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0::3])
it_companies[0] = 'Tesla'
print(it_companies)
it_companies.append('Boring')
print(it_companies)
it_companies.insert(4, 'Snapchat')
print(it_companies)
it_companies[0] = 'FACEBOOK'
print(it_companies)
print(it_companies.sort())
print('FACEBOOK' in it_companies)
print('Tesla' in it_companies)
print('#; '.join(it_companies))
num_list = [20, 25, 58, 73, 56, 48, 49, 27, 15]
print(num_list)
#num_list.sort()
print(num_list)
print(sorted(num_list))
print(num_list)
num_list.sort(reverse=True)
print(num_list)
print(it_companies[0:3])
print(it_companies)
print(it_companies[-1:-4:-1])
print(it_companies[-1::-2])
print(it_companies[3:6])
it_companies.pop(0)
print(it_companies)
it_companies.pop(4)
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
# print(it_companies)
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(8, 'python')
print(full_stack)
full_stack.insert(9, 'SQL')
print(full_stack)
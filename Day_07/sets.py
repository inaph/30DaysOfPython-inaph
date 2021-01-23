it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))
it_companies.add('Twitter')
it_companies.remove('Facebook')
it_companies.update(['Oyo', 'Snapchart'])
print(len(it_companies))
print(it_companies)
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
C = A.difference(B)
D = B.difference(A)
print('Set C: ', C)
print('Set D: ',D)
print(C.union(D))
print(A.symmetric_difference(B))
del A , B, C, D
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages_st = set(age)
print(ages_st)
print(len(age))
print(len(ages_st))
print((len(age))> (len(ages_st)))

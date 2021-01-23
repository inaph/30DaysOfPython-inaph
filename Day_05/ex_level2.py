ages = [19, 22, 19, 24, 20, 25, 20, 28, 31, 55, 81,26, 18, 19, 35, 24, 25, 24]
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
ages.append(19)
ages.append(26)
print(ages)
mid =  (len(ages)) // 2
print(mid)
median_ages = (ages[mid] + ages[~mid])/2
print(median_ages)
print(len(ages))
print(sum(ages))
average_ages = sum(ages)/len(ages)
print(average_ages)
range_ages = max(ages) - min(ages)
print(range_ages)
min_avg = min(ages) - average_ages
max_avg = max(ages) - average_ages
print(min_avg)
print(max_avg)
absolute_ages = abs(min_avg)
print(absolute_ages)
absolute_ages2 = abs(max_avg)
print(absolute_ages2)
Countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(len(Countries_list))
print(Countries_list[3])
print(Countries_list[0:3])
print(Countries_list[3:])
ch, ru, us, *Scandic = Countries_list
print(ch)
print(ru)
print(us)
print(*Scandic)



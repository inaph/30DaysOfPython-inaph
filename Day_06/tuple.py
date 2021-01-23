emty_tpl = ()
print(emty_tpl)
siblings_m = ('teja', 'kushal', 'anji')
siblings_f = ('mahi', 'ammu')
siblings = siblings_f + siblings_m
print(siblings)
print(len(siblings))
parents = ('amma', 'nanna')
family = parents + siblings
print(family)
a,b,c,*rest = family
print (a)
print (b)
print (c)
fruits_tp = ('apple', 'banana','orange')
vegetables_tp = ('brinjal', 'beans', 'cabbage')
animal_prodct_tp = ('chicken', 'fish', 'mutton')
food_stuff_tp = fruits_tp + vegetables_tp  + animal_prodct_tp
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
print(len(food_stuff_lt))
print(food_stuff_lt[4])
print(food_stuff_tp[4])
print(food_stuff_lt[0:3])
print(food_stuff_lt[-4:-1])
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)



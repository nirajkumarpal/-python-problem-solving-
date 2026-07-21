import mymodule
print(mymodule.generate_full_name('Mukesh','panauti'))


# many function in the module and importing them differently

from mymodule import generate_full_name,sum_two_nums,person,gravity
print(generate_full_name('Mukesh','panauti'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])

#Import Functions from a Module and Renaming

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100 
weight = mass * g
print(weight)
print(p)
print(p['firstname'])

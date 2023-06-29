d1 = {}

d2 = dict()

my_dick={
    "name": "Anik",
    "role" : "engineer",
    "company":"TCS",
}
print (my_dick['role'])
print(my_dick.get('role'))
my_dick['salary'] = 1000
my_dick['name'] = "anik saha"
my_dick.update({"hobby":"singing"})
"""
print(my_dick.keys())
print(my_dick.values())
print(my_dick.items())
"""
for key in my_dick.keys():
    print(key)
    
for value in my_dick.values():
    print(value)

    for key,value in my_dick.items():
         print(key,value)

##print(my_dick)


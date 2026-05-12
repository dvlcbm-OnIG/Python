capitals = { "USA" : "Washington D.C",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow",}


if capitals.get("USA"):
    print('That capital exist')

else:
    print("That capital doesn't exist")



capitals.update({"Philippines": "Manila", "Japan": "Tokyo","Russia": "baddie"})  

capitals.update({"Russia": "Thick"})
print(capitals)
print()

keys = capitals.keys()
values = capitals.values()

print(keys)
print(values)


#prints all the KEY inside the dictionary
print()
for key in capitals.keys():
    print(key)

#prints all the VALUE inside the dictionary 
print()
for value in capitals.values():
    print(value)


print()
items = capitals.items()
print(items)

print()
for key, value in capitals.items():
    print(f"{key}: {value}")
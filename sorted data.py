data = (2, 5, 7, 3, 6)
sd = sorted(data, reverse=True)
sd2 = sorted(data)

print(data)
print(sd)
print(sd2)


# sorted data by a key of a dictionnary in a list of dico
dico = [
    {"name": "carlos", "age": 38},
    {"name": "Momo", "age": 20},
    {"name": "ekwe", "age": 26}
]

sorted_data = sorted(dico, key=lambda x: x['age'])
print(sorted_data)

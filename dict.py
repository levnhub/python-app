# Different type keys
dictSample = {4: 3, True: 2, (5, 6): 2}
print(dictSample)

# Dict by method
# country = dict(code="RU", name="Russian")

# Simple dict
country = {"code": "RU", "name": "Russia", "population": 144}
print(country["name"])

# Keys only loop
for key in country:
    print(key)

print(country.items())
# Keys & value loop
for key, value in country.items():
    print(key, "—", value)

# Methods
print(country.keys())
print(country.values())
print(country.get("population"))
print(country.pop("name"))
print(country.popitem())  # remove last element
# print(country.clear())
country.update({"code": "EN"})
country["code"] = "EN"

print(country)

person = {
    "user_1": {
        "first_name": "Lev",
        "last_name": "N",
        "age": 37,
        "address": ["Saint-P", "Morskaya", "41"],
        "grade": {"math": 3, "phisics": 3},
    },
    "user_2": {},
}

print(person["user_1"]["address"][1])

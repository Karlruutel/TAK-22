me = {
    "first_name": "Karl",
    "last_name": "Rüütel",
    "birth_year": 2006,
    "place_of_living": "Upa",
    "dessert": "Puding"
}

print(me.get("place_of_living"))
print(me["place_of_living"])

me["dessert"] = "ice cream"

for key in me:
    print(me[key])
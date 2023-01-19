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

for k, v in me.items():
    print(k, v)

#me["personal_code"] = "3295738104"

me.pop("birth_year")

print(len(me))

if "personal_code" in me:
    print("Isikukood on olemas")
else:
    print("Isikukood ei ole olemas")
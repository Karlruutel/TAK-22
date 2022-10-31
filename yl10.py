user = input("nimi:")
print("tere,", user + "!")

living_place = input("elukoht:")
if living_place.lower() == "saaremaa":
    print("Ööööö, lahe!")

age = int(input("vanus:"))
if age < 18:
    print("Liiga noor, et autot juhtida")
elif age == 18:
    print("palju õnne!")
else:
    print("võid autot juhtida")
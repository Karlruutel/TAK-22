a = int(input("Sisesta aasta number:"))

if a % 400 ==0 or (a % 4 ==0 and a % 100 != 0):
    print( a, "on liigaasta")
else:
    print( a,"on lihtaasta")

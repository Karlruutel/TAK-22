letters = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
i = 0

text = input("Tekst: ")

for c in text:
    if c.lower() in letters:
        i += 1

print("täishäälikute arve tekstis on", i)
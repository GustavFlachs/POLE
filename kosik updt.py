zbozi = ["CPU", "GPU", "RAM", "Motherboard", "Zdroj"]
kosik = []
#################################################### NEFUNGUJE!!!!!!
def vypis_kosik(prvek):
  for x in range(len(prvek)):
        print(f"zbozi číslo {x+1}: {prvek[x]}")
####################################################
def vypis_pole(prvek):
  for x in range(len(prvek)):
        print(f"zbozi číslo {x+1}: {prvek[x]}")
print("---------------------")
vypis_pole(zbozi)
print("---------------------")

print("Vyberte zboží které si chcete přidat do košíku: ")

vyber = int(input())
if 0<vyber<=len(zbozi):
    kosik.append(zbozi[vyber])
    vypis_kosik()
    vypis_pole(kosik)
    zbozi.pop(vyber)

zbozi.pop(vyber)
print(kosik)
print(zbozi)
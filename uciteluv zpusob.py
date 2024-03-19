cislo = int(1) #tohle je pro datový typ celých čísel#
cislo_float = float(3.23)  #datový typ pro desetiná čísla#
text = str("String je sada zákonů, například pro text")
Boolean = True
          #0        1       2     3         4         5      : NULA JE ČÍSLO
arrays =["ford","porsche","audi","BMW","mercedes","Škoda"]

print(arrays) #vypíše celý pole aka list#
#print(arrays[1]) vypíše specifickou věc z listu#
#print(arrays[6]) crash programu bo není šestý

for x in range(len(arrays)):
    print(f"{x+1}): {arrays[x]}")

#UČITELŮV ZPŮSOB#
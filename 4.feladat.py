def alvas(ev, ho, nap):
    honap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(ev%4== 0):
        honap[1] += 1
    if ho>12 or ho<1:
        return print("Nincs ilyen dátum")
    if nap>honap[ho-1] or nap<1:
        return print("Nincs ilyen dátum")


alvas(2000, 2, 29)

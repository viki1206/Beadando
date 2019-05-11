def alvas(ev, ho, nap):
    honap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(ev%4== 0):
        honap[1] += 1
    if ho>12 or ho<1:
        return print("Nincs ilyen dátum")
    if nap>honap[ho-1] or nap<1:
        return print("Nincs ilyen dátum")
    if(ho==12 and nap>6):
        ej=365-nap+6
        if((ev+1)%4==0):
            ej+=1
    elif(ho==12 and nap<=6):
        ej=6-nap
    else:
        ej=6+honap[ho-1]-nap
        for i in range (ho,11):
            ej+=honap[i]
    return print(ej)

alvas(2000, 1, 29)

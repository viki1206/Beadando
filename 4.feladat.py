def alvas(ev, ho, nap):
    honap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if(ev%4== 0):
        honap[1] += 1
    if ho>12 or ho<1:
        return print("Nincs ilyen hónap")



alvas(2000, 4, 5)

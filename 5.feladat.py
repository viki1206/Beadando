def sorozat(a):
    h = []
    e = []
    num = 0
    db = 0
    for j in range(0, len(a) - 1):
        h.append(a[j])
        for k in range(j + 1, len(a) - 1):
            for i in range(k, len(a)):
                if h[db] < a[i]:
                    h.append(a[i])
                    db += 1
            if num < len(h):
                e = h
                num = len(h)
                h = [a[j]]
                db = 0
            else:
                h = [a[j]]
                db = 0
    print(num, ': ', e)

sor = [1, 7, 3, 5, 4, 2]
sorozat(sor)





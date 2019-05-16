def sorozat(a): 
    h = [] 
    e = [] 
    for j in range(0, len(a) - 1): 
        h.append(a[j]) 
        for k in range(j + 1, len(a) - 1): 
            for i in range(k, len(a)): 
                if h[len(h)-1] < a[i]: 
                    h.append(a[i]) 
            if len(e)< len(h):
                e = h 
                h = [a[j]] 
            else:
                h = [a[j]] 
    print(len(e), ': ', e)
sor = [1, 7, 3, 5, 4, 2]
sorozat(sor)


def pref_suf(w1, w2):
    n_letra, pref = 0, ''
    while(len(w1) > n_letra < len(w2)):
        if not (w1[n_letra] == w2[n_letra]):
            break
        pref    += w1[n_letra]
        n_letra += 1
    
    w1   = w1.replace(pref, '')
    w1   = w1 if w1 else 'None'
    w2   = w2.replace(pref, '')
    w2   = w2 if w2 else 'None'
    pref = pref if pref else 'None'

    return ( pref, w1, w2 )

w1 = input()
w2 = input()

print(pref_suf(w1, w2))

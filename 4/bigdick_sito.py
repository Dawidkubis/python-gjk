# Tak tady bude nejaka cool implementace erastotenova sita
# timhle se radsi zatim netrapte
from functools import reduce
def gen_primes(lim): # kratsi nazev -> optimalizace :D
    return [i for i in reduce((lambda a, b : [(i[0] if i[0]==i[1] else 0) for i in zip(a,b)]),[[(0 if ((x % i == 0) and (x != i)) else x) for x in range(2, lim)] for i in range(2, lim)]) if i != 0] # hehe :D
# lol tohle je doslova nenormalni
# prosim nepiste takovyhle kod, nikdo tomu nebude rozumet
# ale je to celkem flex

print(gen_primes(int(input("zadej cislo : "))))

# je to dost pomalejsi nez to predtim ale je to rozhodne vic cool

# vic_bigdick_sito.py
```python
# Sire Kubisi, tady jsem vas dobehl
# Tohle single line sito je lepsi, kratsi a rychlejsi
# (Meril jsem to pomoci timeit)

from functools import reduce

def primes(n):
    return reduce(lambda l, x: [y for y in l if y==x or y%x!=0], range(2, n), range(2, n))

print(primes(int(input("Zadej cislo: "))))
```
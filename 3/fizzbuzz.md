# fizzbuzz.py
```python

# tahame hodnotu od uzivatele
lim = int(input('zadej cislo : '))

# prazny string
output = ''
# vsechna cisla do lim
for i in range(lim):
    # reset promenny output
    output = ''

    # pokud delitelne tremi
    if i % 3 == 0:
        output += 'fizz'
    # pokud delitelne peti
    if i % 5 == 0:
        output += 'buzz'
    
    # zjistujeme jestli nam to
    # stoji za to vypsat
    if output != '':
        print(output)
```
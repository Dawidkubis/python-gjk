# sude_nebo_liche.py
```python

# zjistujeme cislo od uzivatele
x = input('zadej cislo : ') # x je typ str
# prevadime x na typ int pomoci funkce `int`
# tohle vyhodi chybu pokud uzivatel je dement
# a napsal neco ve smyslu 'ahoj'; to totiz nelze prevest na int
x = int(x)

# koukame se jestli zbytek z deleni dvemi je 0
# -> jesli je `x` delitelne dvemi
if x % 2 == 0:
    print('je sude')
else:
    # tohle je sice ekvivalent `elif x % 2 == 1`
    # ale takhle je to prehlednejsi
    # mohli bychom taky napsat dalsi if
    # - fungovalo by to stejne ale tohle je
    # mnohem prehlednejsi
    print('je liche')
```
# Datové Typy

V programování existuje pojem datových typů, které specifikují jakého typu může být hodnota v proměnné.

## Staticky a dynamicky typované jazyky

Staticky typované jazyky vyžadují specifikaci typu proměnné při její deklaraci (některé si typy doplňují při kompilaci a není potřeba je tam psát).

Dynamicky typované jazyky kontrolují typy při spouštění programu a tudíž se typy proměnných můžou měnit v průběhu práce.

Python je dynamicky typovaný jazyk : 
```python
>>> x = 3
>>> x
3
>>> x = 'foo'
>>> x
'foo'
```

## Datové Typy

### int
Typ `int`(integer) je typ který popisuje nějaké celé číslo, kladné nebo záporné.
V Pythonu vypadá takhle : 
```python
>>> x = 2 # tohle je int
>>> x = -32 # tohle je taky int
```

### float
Typ `float` je typ který popisuje nějaké číslo s destinnou čárkou, kladné nebo záporné.
```python
>>> x = 2.3232 # tohle je float
>>> x = -32.4444 # tohle je taky float
```

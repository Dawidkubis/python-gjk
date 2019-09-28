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

Teď si projedeme několik základních datových typů. Budu tady používat funkci `type()`, o které jsme se sice nezmíňovali ale hodí se na zjišťování datového typu proměnných.

### int
Typ `int` (integer) je typ který popisuje nějaké celé číslo, kladné nebo záporné nebo nulové.
V Pythonu vypadá takhle : 
```python
>>> x = 2 # tohle je int
>>> x = -32 # tohle je taky int
>>> type(x)
<class 'int'>
```

### float
Typ `float` je typ který popisuje nějaké číslo s destinnou čárkou, kladné nebo záporné nebo nulové (psáno jako `0.0`).
```python
>>> x = 2.3232 # tohle je float
>>> x = -32.4444 # tohle je taky float
>>> type(x)
<class 'float'>
```

### str/String
Typ `str` (také `String`) je typ který popisuje nějaký textový řetězec. V Pythonu je do tohoto typu taky zahrnutý takzvaný typ `char`, který popisuje jeden znak.
Řeťezec by měl být obalen uvozovkami (`""`) nebo apostrofy (`''`) aby se dal odlišit od proměnných.
```python
>>> x = 'hello world' # str
>>> type(x)
<class 'str'>
>>>x = 'h' # taky str
>>> type(x)
<class 'str'>
```

### bool
Typ `bool` (také `boolean`) je typ který má dvě možné hodnoty : `True` čili pravda nebo `False`čili nepravda.
Tento typ dokáže přímo pracovat z `if`-ama, jelikož je sám v sobě boolean výrazem.
```python
>>> x = True
>>> x = False
>>> type(x)
<class 'bool'>
```
```python
x = True
if x:
	print('tohle se provede protoze x je pravda tudiz nemusime psat : "if x == True:'")
```


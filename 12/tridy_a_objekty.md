# Třídy a Objekty

Třídy v programování popisují nějaký "typ" určité hodnoty.
Například hodnota `1` je typu `int`, hodnota `'ahoj'` je typu `str` - typy jsou třídy a hodnoty objekty.
Třídy popisují jen obecné vlastnosti a činnosti (funkce, u tříd se jim říká metody).

Objekty jsou instance třídy, které mají nějaké konktrétní hodnoty.

Takhle vypadá definice třídy v pythonu:
```python
class Clovek: # tridy se nazyvaji s velkym pocatecnim pismenem
	def __init__(self, age, height):
		self.age = age # self.age patri objektu, age je argument metody
		self.height = height
```
Metoda `__init__` je tzv. konstruktor, čili je volána vždy když tvoříme objekt.
`self` je proměnná do které se automaticky přiřadí objekt.

Takle vypadá konstrukce objektu třídy člověk:
```python
x = Clovek(18, 180)
```
Je dobré si všimnout, že při konstrukci jsme dali metodě `__init__` jen dva argumenty, i když v definici bere tři.
To je proto, že objekt se automaticky přiřadí k proměnné `self` (nebo jakékoli proměnné která bude na začátku).
Protože `__init__` je konstruktor, tak k self se přiřadí prázdný objekt, kterému potom dáváme nějaké vlastnosti.
Je to lechce podobný proces jako při práci se slovníky:
```python
def init(age, height)
	x = dict()
	x["age"] = age
	x["height"] = height

	return x
```
Až na to, že k datům objektu přistupujeme pomocí tečky (`x.age` místo `x["age"]`).

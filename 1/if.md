# IF

If je blok který vyhodnocuje nějaký boolean výrazu (výrazu který vrací buď `True` nebo `False`)
a provadí určitý kód na základě toho, co dostane

## Příklad

```python

cislo = 12 # tady by mohl byt input() od uzivatele

if cislo % 2 == 0: # jeden blok (if - elif - else)
	# if vzdy zacina blok, tudiz muze byt jen jeden v jednom bloku
	print('cislo je sude') # toto se provede jelikoz 12 % 2 je 0
elif cislo % 3 == 0:
	# elif-u tady muze byt 'nekonecne' mnoho
	print('cislo je delitelne tremi') # toto se neprovede i presto ze 12 % 3 je 0
else:
	# v jednom bloku muze byt else jenom jeden
	print('cislo je liche') # toto by se provedlo kdyby se vsechno nad tim neprovedlo

```

## Další Příklad

```python

cislo = 12

if cislo % 2 == 0: # jeden blok
	print('cislo je sude') # provede se
if cislo % 3 == 0: # dalsi blok (if - else)
	print('cislo je delitelne tremi') # taky se provede
else:
	print('cislo neni delitelne tremi') # neprovede se, patri k if-u nad tim

```

# Tenarni operator
Unarni operatory jsou operatory ktery berou 1 vstup. Napriklad `not` je unarni operator.

Binarni operatory jsou operatory ktery berou 2 vstupy. Napriklad `+` je binarni operator.

Tenarni operator je operator ktery bere 3 vstupy. Ten je v pythonu tedy jenom jeden vypada takto:
```python
n = 2 # nejaky cislo
print("sudy" if n % 2 == 0 else "lichy") # vypise `sudy` protoze n je sudy
```
coz je ekvivalence:
```python
n = 2
if n % 2 == 0:
	print("sudy")
else:
	print("lichy")
```

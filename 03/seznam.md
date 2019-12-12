# Seznamy

Seznamy nám dovolují ukládat hodnoty v seznamu (lol) a pracovat s nima.
Datové typy v seznamech se sice můžou lišit ale je lepší aby všechny
byly stejné. Jednotlivé prvky v seznamech jsou označeny tzv. indexem, 
což je číslo které popisuje kolikátý prvek to je.

```python
>>> x = [1, 2, 3]
>>> x[0] # prvek v `x` s indexem 0
1
>>> x[1]
2
>>> x[2]
3
```

## operace na seznamech

```python
>>> x = [1,2,3]
>>> len(x) # delka x
3
>>> x.append(4) # prida prvek na konec seznamu
>>> x
[1, 2, 3, 4]
>>> x.pop() # odebere prvek z konce seznamu
4
>>> x
[1, 2, 3]
```

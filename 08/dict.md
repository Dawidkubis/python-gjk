# Dict

`dict` je datový typ sloužící k ukládání hodnot pod určitými klíči. Jedná se určitým způsobem o něco jako pole, kde místo číselných indexů používáme libovolné neměnné objekty (čísla, stringy, tuply...)

Příklad:
```python
>>> # Jedno z využití dictonary je snadná reprezentace složených dat
>>> mydict = {'jmeno': 'Lukáš', 'vek': 7893, 'poznamka': 'naposledy jsem to přestal počítat před 7893 lety'}
>>> mydict['vek']
7893
>>> # Za pomocí dictionary můžeme reprezentovat třeba i orientovaný graf.
>>> graph = {0: [2, 3], 1: [1, 0], 2: [3, 1]}
>>> graph[2] # Cesty z vrcholu číslo 2
[3, 1]
```

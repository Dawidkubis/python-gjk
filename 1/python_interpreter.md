# Python Interpreter

Python interpreter je program jež nám umožňuje spustit skript který jsme si napsali.
Pokud je v $PATH (což by měl být) tak ho můžeme volat z příkazového řádku (takhle to vypada u me) :
```shell
$ python
Python 3.7.4 (default, Jul 16 2019, 07:12:58) 
[GCC 9.1.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Když takhle zavoláme Python bez argumentů, tak se interpreter spustí v tzv. interaktivním módu.
Vocaď můžeme Python používat jako kalkulačku, například :
```python
>>> 2 * 3
6
>>> 2 + 3
5
>>> x = 2 * 3
>>> x * 70
420
```
Python nám automaticky vyprintuje hodnout všech výrazů, což je specialita interaktivnícho módu.

Když chceme spustit nějaký soubor s python kódem, musíme přidat cestu k souboru jako argument.

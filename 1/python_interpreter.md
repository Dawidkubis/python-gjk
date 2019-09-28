# Python Interpreter

Python interpreter je program jež nám umožňuje spustit skript který jsme si napsali.
Pokud je v $PATH (což by měl být) tak ho můžeme volat z příkazového řádku (takhle to vypadá u mě) :
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
Python nám automaticky vyprintuje hodnoty všech výrazů, což je specialita interaktivnícho módu.

Když chceme spustit nějaký soubor s python kódem, musíme přidat cestu k souboru jako argument.
```shell
$ python <nazev_skriptu>.py
```
Všechny python skripy by měly končit koncovkou `.py`.
Toto bude fungovat jenom pokud jste ve stejné složce jako je `<nazev_skriptu>.py`, jinak budete muset specifikovat relativní nebo absolutní cestu, případně přejít do složky se skriptem pomocí příkazu `cd`. Více o cestách a shellových příkazech najdete [zde](https://ryanstutorials.net/linuxtutorial/navigation.php) (windowsáci si budou muset v mysli nahradit `ls` za `dir`)

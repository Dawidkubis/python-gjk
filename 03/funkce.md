# Funkce

Funkce jsou jedna z nejpodstatnějších věcí o kterých se budeme bavit.

Funkce nám pomáhají neopakovat kód, jinými slovy díky funkcím můžeme 
znovupoužít kusy kódu.

Funkce slouží jako logické rozdělení toho jak má fungovat náš program.

```python

def fungce():
	print('tahle funkce nema zadny argumenty')

def funkce(argument, dalsi_argument):
	print(argument)
	print(dalsi_argument)

```
```python
>>> fungce()
tahle funkce nema zadny argumenty
>>> funkce('hello', 'world')
hello
world
>>> funkce(1,2)
1
2
```

# Input/Output

Vstup a výstup funkce zajištují argumenty a return hodnoty.

Argumenty píšeme do závorky za názvem funkce.

```python
def funkce(argument, dalsi_argument):
	# .. bla bla bla
	# s argumenty pracujeme jako s promennymi
```

Return píšeme uvnitř funkce.

```python
def funkce():
	return 'ahoj' # tahle funkce vraci 'ahoj' po spusteni
	# return ukonci praci funkce

>>> print(funkce())
ahoj
```

# Pass

`pass` nám dovolí nechat nedopsanou funkci která nevyhodí error 
při interpretaci. Má to svoji funkci když plánujeme co napíšeme a 
tvoříme funkce ale není to podstatný si to pamatovat. Spíše se 
jenom nedivte až to někde uvidíte.

```python
def funkce():
	pass

>>> funkce()
>>> # nic se nestalo lol
```

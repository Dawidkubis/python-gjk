# faktorial_rekurze.py
```python
# tady budeme resit faktorial rekurzivne
# matematicka definice :
#f(0) = 1
#f(n) = n * f(n - 1)
# takze vidime rekurzi - muzeme vyuzit

def f(n):
	if n == 0: # f(0) = 1
		return 1
	# tady nepotrebujeme else, jelikoz v predchozim
	# if-u je return
	return n * f(n - 1) # f(n) = n * f(n - 1)

print(f(3)) # f(3) = 6
# f(3) = 3 * f(2) = 3 * 2 * f(1) = 3 * 2 * 1 * f(0) = 3 * 2 * 1 * 1 = 6

print(f(100)) # je to celkem v pohode, az na to ze python neni uplne
# dobrej pokud jde o rekurzi
# zkuste treba co se stane kdyz udelate :
#print(f(1000))
```
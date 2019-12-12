# List Comprehensions
list comprehensions jsou super.
Dovolujou zkratit kod uplne strasne moc.

Je to prakticky `for` kterej dovoluje filtrovat.

Tohle:
```python
# chceme sebrat vsechna sudo cisla do 1000
n = []
for i in range(1000):
	if i % 2 == 0:
		n.append(i)
print(n)
```
Je ekvivalence:
```python
n = [i for i in range(1000) if i % 2 == 0]
print(n)
```
coz muzeme cist jako: "n je seznam vsech cisel do 1000 kde zbytek z deleni dvemi je nula, tl;dr vsech sudych cisel"

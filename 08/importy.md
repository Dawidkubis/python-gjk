# Importy
Importy nam slouzi k organizaci kodu nebo pouzivani kodu kterej napsal nekdo jinej.

# Importovani vlastniho kodu

Rekneme ze mate takovouhle slozku:
```
.
├── lib.py
└── main.py
```
lib.py:
```python
def hello(jmeno):
    return "hello " + jmeno

print("tohle je modul lib.py") # pozor; tohle se spusti, hned vysvetlim
```
main.py:
```python
import lib # ne `import lib.py`

print(lib.hello("world")) # ne `hello("world")` ale `lib.hello("world")`
```
Kdyz pak udelame `python main.py` a spustime tim program tak dostaneme:
```
tohle je modul lib.py # <- tohle dostaneme protoze pri importu se `lib.py` jakoby spusti, to ale nechceme
hello world # <- tohle je vystup z main.py, to co jsme chteli
```
Prave proto si davejte pozor co pisete do veci ktery pak importujete, idealne by neco mel delat jenom
jeden soubor a zbytek by mel byt plny funkci (nic nedelat) abyste se nedostali k situaci kdy
se vam neco posralo hledate to mezi vsema python souborama.

# Importovani cizicho kodu

Cizi kod muzeme ziskat tim, ze si ho stahneme pomoci `pip`u z oficialnich repositari python moduluu.

Ukazeme si to na prikladu modulu `requests`, ktery nam dovoluje vyrizovat http requesty v pythonu.

Zacneme tim ze si ho stahneme:
```shell
pip install requests
```
nebo na nekterych kompech:
```shell
python -m pip install requests
```
Pak pockame az se stahne requests a muzeme pouzivat:

```python
import requests

a = requests.get("https://raw.githubusercontent.com/Dawidkubis/python-gjk/master/8/importy.md")
print(a.text)
```
Schvalne zkuste co vam to vypise :D

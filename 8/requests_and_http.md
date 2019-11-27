# Http
Http je zpusob komunikace ktery se pouziva na siti.

Http posila data, vetsinou ve formatu `html`, kterej nespis znate ale neplette si ty pojmy.
Http zacina headerem kterej popisuje:

+ jestli je to pozadavek nebo odpoved (request & response)
+ pokud je to odpoved tak jestli doslo k nejaky chybe
+ pokud je to pozadavek tak co se vlastne po tom serveru chce

# Http metody
+ GET - chceme ziskat obsach, vetsinou html, ze serveru. Neposilame zadny data
+ POST - chceme neco postnout na server, posilame data v nejakym formatu (vetsinou `json`)
Je jich vic, ale to tady nebudu rozebirat. Pokud vas to zajima tak si to vygooglete.

# Requests
Requests nam dovoli pracovat s tema http metodama a posilat http pozadavky (requesty - proto `requests`).

## GET
```python
import requests # viz. importy.md
response = requests.get("https://google.com") # posilame GET na google
# tohle se bezne deje kdyz nacitame tu stranku v prohlizeci
print(response.text) # html ktery jsme dostali zpatky, prohlizec tyto data zpracuje
		     # aby to nejak hezky vypadalo
		     # responese ma jeste mnoho veci ktery jsme mohli tahat
		     # treba:
		     #response.status_code
		     # atd, ale to nebudu rozebirat, proste se s tim da delat hromada veci
```
## POST
To tady nebudu resit, ted se mi to nechce psat

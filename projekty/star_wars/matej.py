import requests

# wtf jsou tyhle obrovsky mezery

def ship_detail(ShipName):
    url = 'https://swapi.co/api/starships'
    r = requests.get(url).json() # ^-- tohle je mega gay, protoze si nacitas vsechny data
    res = r['results']			 # a sortujes v pythonu, misto toho abys si upravil
    ship_absolute = ''			 # url - mel bys to jednodussi, rychlejsi, prehlednejsi
    for ship in res:			 # a pametove efektivnejsi
        if ship['name'] == ShipName: # lol
            ship_absolute = ship
            break
    return[ship_absolute['name'], ship_absolute['model'], [requests.get(film).json()['title'] for film in ship_absolute['films']]] # sexy

def species_detail(SpeciesName):
    url = 'https://swapi.co/api/species' # stejnej problem jako nahore
    r = requests.get(url).json()
    res = r['results']
    species_absolute = '' # eeh, celkem dlouhej nazev, sice to neni explicitni chyba ale kratsi nazev = lepsi nazev
    for specie in res:
        if specie['name'] == SpeciesName:
            species_absolute = specie
            break
    list_title = [requests.get(film).json()['title'] for film in species_absolute['films']]
    list_id = [requests.get(film).json()['episode_id'] for film in species_absolute['films']]
    sort = sorted(zip(list_id, list_title))
    return [species_absolute['name'], species_absolute['classification'], species_absolute['designation'], requests.get(species_absolute['homeworld']).json()['name'], sort] # sexy


def person_detail(Name): # a zase
    url = 'https://swapi.co/api/people'
    r = requests.get(url).json()
    res = r['results']
    person_absolute = ''
    for person in res:
        if person['name'] == Name:
            person_absolute = person
            break

    list_title = [requests.get(film).json()['title'] for film in person_absolute['films']]
    list_id = [requests.get(film).json()['episode_id'] for film in person_absolute['films']]
    sort = sorted(zip(list_id, list_title))
    return [person_absolute['name'], person_absolute['gender'], requests.get(person_absolute['homeworld']).json()['name'], sort] # sexy

def Crawl(Film_Title): # a poctvrte
    url = 'https://swapi.co/api/films'
    r = requests.get(url).json()
    res = r['results']
    film_absolute = ''
    for film in res:
        if film['title'] == Film_Title:
            film_absolute = film # <-- mozny vynechat protoze film == film_absolute je True
            break				 # protoze film se updateuje kazdou loopu - kdyz loop skonci (`break`) tak film je promenna po breaku
        						 # coz je hezky protoze recyklujes promenne aniz by jejich nazev
        						 # neodpovidal hodnote
    print(film_absolute['opening_crawl'])


def film_detail(FilmIdentifier): # a popate :D
    url = 'https://swapi.co/api/films'
    r = requests.get(url).json()
    res = r['results']
    film_absolute = ''
    for film in res:
        if film['title'] == FilmIdentifier or film['episode_id'] == FilmIdentifier:
            film_absolute = film
            break
    list_char = [requests.get(char).json() for char in film_absolute['characters']]
    list_ship = [requests.get(char).json() for char in film_absolute['starships']]
    return [film_absolute['title'], film_absolute['director'], film_absolute['episode_id'], sorted([ch['name'] for ch in list_char]), sorted([ch['name'] for ch in list_ship])] # sexy


if __name__ == '__main__':
    print(ship_detail('Executor'))
    print(species_detail('Hutt'))
    print(person_detail('Luke Skywalker'))
    print(film_detail(3))
    print(film_detail('A New Hope'))
    Crawl('The Phantom Menace')

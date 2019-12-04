# petr.py
```python
import requests
import json
import time


# helper functions - Pedro
# nice, delas abstrakce coz je super
def get_json(url):
    return requests.get(url).json()

# dalsi abstrakce, hmm
# asi celkem v pohode, ale nazvy potencialne moc dlouhy
def get_film_titles(films):
    list_films = []
    for film in films:
        list_films.append(get_json(film)["title"])
    # mohl si napsat:
    #return [get_json(film)["title"] for film in films]
    return list_films


def get_character_names(characters):
    list_characters = []
    for character in characters:
        list_characters.append(get_json(character)["name"])

    return sorted(list_characters) # asi ne uplne dobry volat na tom sorted
								   # ztracis trochu generalizaci
								   # ale to je fakt detail 

def get_spaceship_names(spaceships):
    list_spaceships = []
    for spaceship in spaceships:
        list_spaceships.append(get_json(spaceship)["name"])

    return sorted(list_spaceships)


def get_film_info(film):
    list_characters = get_character_names(film["characters"])
    list_spaceships = get_spaceship_names(film["starships"])
    return [film["title"], film["director"], film["episode_id"],
                         list_characters, list_spaceships] # kdyz uz takhle formatujes tak
    													   # muzes rovnou na vic radku


def ship_detail(shipname):
    web = get_json("https://swapi.co/api/starships/?search={}".format(shipname))["results"]
    list_results = []
    for result in web:
        list_films = get_film_titles(result["films"])
        list_results.append(
            [result["name"], result["model"], result["starship_class"], result["hyperdrive_rating"], list_films])

    return list_results


def species_detail(speciesname):
    web = get_json("https://swapi.co/api/species/?search={}".format(speciesname))["results"]
    list_results = []
    for result in web:
        list_films = get_film_titles(result["films"])
        homeworld = get_json(result["homeworld"])["name"]
        list_results.append(
            [result["name"], result["classification"], result["designation"], homeworld, list_films])

    return list_results


def person_detail(name):
    web = get_json("https://swapi.co/api/people/?search={}".format(name))["results"]
    list_results = []
    for result in web:
        list_films = get_film_titles(result["films"])
        homeworld = get_json(result["homeworld"])["name"]
        list_results.append(
            [result["name"], result["gender"], homeworld, list_films])

    return list_results


def film_detail(filmidentifier, id_type="ep_id"):
    list_results = []
    if id_type == "ep_id":
        web = get_json("https://swapi.co/api/films/{}".format(filmidentifier))
        list_results.append(get_film_info(web))
    elif id_type == "title":
        web = get_json("https://swapi.co/api/films/?search={}".format(filmidentifier))["results"]
        for result in web:
            list_results.append(get_film_info(result))

    else:
        raise Exception('Bad film id type') # eeh, ok

    return list_results


def crawl(title):
    web = get_json("https://swapi.co/api/films/?search={}".format(title))["results"]
    for result in web:
        film_crawl = result["opening_crawl"].split("\r\n")
        for line in film_crawl:
            print(line)
            time.sleep(1)


if __name__ == "__main__":
    # testing program. runs only if run as main - Pedro
    print(ship_detail("Imperial shuttle"))
    print(species_detail("Hutt"))
    print(person_detail("Owen Lars"))

    print(film_detail("The Phantom Menace", "title"))
    print(film_detail(2))

    crawl("A New Hope")

# shit Pedro mas to moc dobry, priste to udelej hur pls
```
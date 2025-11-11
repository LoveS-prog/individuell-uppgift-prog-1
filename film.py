

import json

FILM_FILE = "films.json"  # En global variabel för filnamnet


class Film:
    """En film med titel, år och betyg."""

    def __init__(self, title: str, year: int, rating: float):
        self.title = title  # Sätter filmens titel
        self.year = int(year)  # Gör om år till int
        self.rating = float(rating)  # Gör om betyg till float


def save_json(data, filename: str):
    """Sparar data till json filen."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # Skriver data till filen


def load_json(filename: str):
    """Läser in data från json filen."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)  # Läser in och returnerar data från filen
    except:
        return None  # Om filen inte finns eller inte fungerar så returnerar den None


def load_films():
    """Skriver ut alla filmer i en lista."""
    data = load_json(FILM_FILE)  # Läser in data från filen
    if not data or "films" not in data:  # Om filen är tom eller saknar rätt key så returnerar den en tom lista
        return []
    films = []
    for film_dict in data["films"]:
        title = film_dict.get("title", "")  # Plockar ut titel
        year = film_dict.get("year", 0)  # Plockar ut år
        rating = film_dict.get("rating", 0)  # Plockar ut betyg
        films.append(Film(title, year, rating))  # Lägger till filmen i listan
    return films


def save_films(films):
    """Sparar alla filmer till filen."""
    data = {"films": []}
    for film in films:
        data["films"].append({
            "title": film.title,  # Lägger till titel i dict
            "year": film.year,    # Lägger till år i dict
            "rating": film.rating,  # Lägger till betyg i dict
        })
    save_json(data, FILM_FILE)  # Sparar dict till fil


def find_film(films, title):
    """Letar efter en film som har exakt samma titel."""
    title = title.lower()  # .lower() gör så att om du skriver med stora eller små bokstäver spelar ingen roll
    for film in films:
        if film.title.lower() == title:  # Jämför också med små bokstäver
            return film
    return None  # Returnerar None om ingen film hittades


def list_films(films):   
    """Skriver ut alla filmer i en lista."""
    if not films:
        print("Inga filmer hittas")
        return
    for film in films:
        print(film.title, film.year, film.rating)  # Skriver ut titel, år och betyg


def add_film(films):
    """Lägger till en film genom input från användaren."""
    title = input("Titel: ")  # Frågar efter titel
    if not title:
        print("Du måste skriva en titel.")
        return
    year = input("År: ")  # Frågar efter år
    rating = input("Betyg: ")  # Frågar efter betyg
    films.append(Film(title, year, rating))  # Lägger till filmen i listan
    save_films(films)  # Sparar filmerna till filen
    print("Film sparad.")


def update_rating(films): 
    """Ändrar betyg på en film."""
    title = input("Film att ändra betyg på: ")  # Frågar vilken film som ska ändras
    film = find_film(films, title)  # Letar upp filmen
    if not film:
        print("Hittas inte.")
        return
    new_rating = input("Nytt betyg: ")  # Frågar efter nytt betyg
    film.rating = Film(film.title, film.year, new_rating).rating  # Gör om det nya betyget till ett tal
    save_films(films)  # Sparar filmerna till filen
    print("Uppdaterat.")


def remove_film(films):
    """Tar bort en film från listan."""
    title = input("Film att ta bort: ")  # Frågar vilken film som ska tas bort
    film = find_film(films, title)  # Letar upp filmen
    if not film:
        print("Hittas inte.")
        return
    films.remove(film)  # Tar bort filmen från listan
    save_films(films)  # Sparar filmerna till filen
    print("Borttagen.")


def search_title(films):   # Söker igenom alla filmer och skriver ut de som innehåller det du söker efter i titeln
    """Söker filmer där titeln innehåller det du skriver."""
    text = input("Sök film: ").lower()  # .lower() gör så att om du skriver med stora eller små bokstäver spelar ingen roll
    if not text:
        print("Du måste skriva något för att söka.")
        return
    found = []
    for film in films:
        if text in film.title.lower():  # Kollar om det du söker finns någonstans i filmens titel oavsett stora eller små bokstäver
            found.append(film)
    if not found:
        print("Hittade inte.")
        return
    for film in found:
        print(film.title, film.year, film.rating)  # Skriver ut alla filmer som matchade sökningen

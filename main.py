

import film  # Importerar hela film.py filen


if __name__ == "__main__":
    films = film.load_films()  # Låser in sparade flimer från json filen


    while True:
        # Visar menyval, den anropar funktioner i film.py, man kan välja val mellan 0-5 
        print("Filmregister")
        print("1 Visa lista på filmer")  
        print("2 Lägg till film")    
        print("3 Ändra betyg på film") 
        print("4 Ta bort film")     
        print("5 Sök titel")         
        print("0 Avsluta")           
        choice = input("> ")  # Här skriver man in val mellan 0-5


        if choice == "1":
            film.list_films(films)   # Skriver ut alla filmer
            input("Tryck Enter...")
        elif choice == "2":
            film.add_film(films)     # Lägger till film
            input("Tryck Enter...")
        elif choice == "3":
            film.update_rating(films)  # Ändrar betyg
            input("Tryck Enter...")
        elif choice == "4":
            film.remove_film(films)    # Tar bort film
            input("Tryck Enter...")
        elif choice == "5":
            film.search_title(films)   # Söker på titel
            input("Tryck Enter...")
        elif choice == "0":
            film.save_films(films)     # Sparar innan programmet avslutas
            print("Programmet avslutas.")
            break
        else:
            print("Fel val.")          # Om man skriver fel val

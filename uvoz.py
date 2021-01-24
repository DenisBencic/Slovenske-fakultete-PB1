import sqlite3 as dbapi

def uvozi():
    '''
    Uvozi in ustvari bazo, če ta ne obstaja,
    ter vrne število elementov vsake tabele.
    '''

    # Ustvari povezavo in kurzor
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()

    kurzor.execute("SELECT COUNT(*) FROM sqlite_master")
    if kurzor.fetchone() == (0, ):

        # Branje iz datotek
        with open('data/tabele.sql', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])

        with open('data/univerza.sql', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])

        with open('data/fakulteta.sql', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])


        with open('data/program.sql', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])

    # Prekinitev povezave z SQL
    povezava.commit()
    kurzor.close()
    povezava.close()


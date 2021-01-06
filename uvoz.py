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
        with open('tabele.txt', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])

        with open('univerza.txt', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])

        with open('fakulteta.txt', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])


        with open('program.txt', 'r', encoding = 'utf-8') as datoteka:
            for vrstica in datoteka:
                # Odstranimo '\n' v prebranih ukazih, 
                kurzor.execute(vrstica[:-1])

    # Določanje uvodnih parametrov - število entitet
    kurzor.execute('SELECT COUNT(*) FROM univerza')
    st_univerz = kurzor.fetchone()[0]
    kurzor.execute('SELECT COUNT(*) FROM fakulteta')
    st_fakultet = kurzor.fetchone()[0]
    kurzor.execute('SELECT COUNT(*) FROM program')
    st_programov = kurzor.fetchone()[0]

    # Prekinitev povezave z SQL
    povezava.commit()
    kurzor.close()
    povezava.close()

    return (st_univerz, st_fakultet, st_programov)

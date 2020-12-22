import sqlite3 as dbapi

# Ustvari povezavo in kurzor
povezava = dbapi.connect('SlovenskeFakultete.sqlite')
kurzor = povezava.cursor()

# Izbriše že obstoječe tabele, če so
kurzor.execute('DROP TABLE IF EXISTS univerza;')
kurzor.execute('DROP TABLE IF EXISTS fakulteta;')
kurzor.execute('DROP TABLE IF EXISTS program;')

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

# Določanje uvodnih parametrov
kurzor.execute('SELECT COUNT(*) FROM univerza')
st_univerz = kurzor.fetchone()[0]
kurzor.execute('SELECT COUNT(*) FROM fakulteta')
st_fakultet = kurzor.fetchone()[0]
kurzor.execute('SELECT COUNT(*) FROM program')
st_programov = kurzor.fetchone()[0]

# Pozdrav uporabnika
print('Pozdravljeni v bazi slovenskih univerz, fakultet in programov.')
print('V bazi je trenutno {} univerz, {} fakultete in {} programov.'.format(st_univerz - 1, st_fakultet, st_programov))

# Prekinitev povezave z SQL
povezava.commit
kurzor.close
povezava.close



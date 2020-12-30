import sqlite3 as dbapi
from bottle import route, run, template

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

@route('/')
def pozdrav():
    return '''
        <!DOCTYPE html>
        <head>
            <title> Slovenske fakultete </title>
        </head>
        <body>
        <p><b>Pozdravljeni v bazi slovenskih univerz, fakultet in programov.
        <br>V bazi je trenutno {} univerz, {} fakultete in {} programov.
        </b>
        <br>
        <br> Kaj želite iskati?
            <ol>
                <li> <a href = '../univerze/'> Univerze </a> </li>
                <li> <a href = '../fakultete/'> Fakultete </a> </li>
                <li> <a href = '../programi/'> Programi </a> </li>
            <ol>
        </p>
        </body>
        </html>
    '''.format(st_univerz - 1, st_fakultet, st_programov)

@route('/fakultete/')
def fakultete():
    html = f"<a href = '../'> Nazaj </a>"
    return html

@route('/univerze/')
def univerze():
    html = f"<a href = '../'> Nazaj </a>"
    return html

@route('/programi/')
def programi():
    html = f"<a href = '../'> Nazaj </a>"
    return html

run(debug = True)

# Prekinitev povezave z SQL
povezava.commit
kurzor.close
povezava.close

from bottle import route, run, template, request
from uvoz import uvozi
from iskalne_funkcije import *

uvozi()

@route('/')
def pozdrav():
    return template('zacetna_stran.html')

@route('/univerze/')
def univerze():
    return template('univerze.html')

@route('/univerze/naziv/')
def naziv():
    return template('isci_univerze_naziv.html')

@route('/univerze/tip/')
def tip():
    return template('isci_univerze_tip.html')

@route('/univerze/rektor/')
def rektor():
    return template('isci_univerze_rektor.html')

@route('/univerze/lokacija/')
def rektor():
    return template('isci_univerze_lokacija.html')

@route('/univerze/kontakt/')
def kontakt():
    return template('isci_univerze_kontakt.html')

@route('/univerze/e_naslov/')
def e_naslov():
    return template('isci_univerze_e_naslov.html')

@route('/univerze/spletna_stran/')
def spletna_stran():
    return template('isci_univerze_spletna_stran.html')

@route('/univerze/leto_ustanovitve/')
def leto_ustanovitve():
    return template('isci_univerze_leto_ustanovitve.html')

@route('/fakultete/')
def fakultete():
    return template('fakultete.html')

@route('/fakultete/naziv/')
def naziv():
    return template('isci_fakultete_naziv.html')

@route('/fakultete/dekan/')
def dekan():
    return template('isci_fakultete_dekan.html')

@route('/fakultete/lokacija/')
def lokacija():
    return template('isci_fakultete_lokacija.html')

@route('/fakultete/kontakt/')
def kontakt():
    return template('isci_fakultete_kontakt.html')

@route('/fakultete/e_naslov/')
def e_naslov():
    return template('isci_fakultete_e_naslov.html')

@route('/fakultete/spletna_stran/')
def spletna_stran():
    return template('isci_fakultete_spletna_stran.html')

@route('/fakultete/leto_ustanovitve/')
def leto_ustanovitve():
    return template('isci_fakultete_leto_ustanovitve.html')

@route('/fakultete/univerza/')
def univerza():
    return template('isci_fakultete_univerza.html')
    
@route('/programi/')
def programi():
    return template('programi.html')

@route('/programi/naziv/')
def naziv():
    return template('isci_programi_naziv.html')

@route('/programi/redni/')
def redni():
    return template('isci_programi_redni.html')

@route('/programi/izredni/')
def izredni():
    return template('isci_programi_izredni.html')

@route('/programi/stopnja/')
def stopnja():
    return template('isci_programi_stopnja.html')

@route('/programi/fakulteta/')
def fakulteta():
    return template('isci_programi_fakulteta.html')

@route('/programi/univerza/')
def fakulteta():
    return template('isci_programi_univerza.html')

@route('/univerze/naziv/rezultati/')
def isci():
    iskalni_niz = request.query['iskalni_niz']
    univerze = isci_univerza_naziv(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/tip/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_tip(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/rektor/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_rektor(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/lokacija/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_lokacija(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/kontakt/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_kontakt(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/e_naslov/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_e_naslov(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/spletna_stran/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_spletna_stran(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/univerze/leto_ustanovitve/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    univerze = isci_univerza_leto_ustanovitve(iskalni_niz)
    return template('rezultati_iskanja_univerze', iskalni_niz = iskalni_niz, univerze = univerze)

@route('/fakultete/naziv/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_naziv(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/dekan/rezultati/')
def isci():
    iskalni_niz = request.query['iskalni_niz']
    fakultete = isci_fakulteta_dekan(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/lokacija/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_lokacija(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/kontakt/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_kontakt(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/e_naslov/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_e_naslov(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/spletna_stran/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_spletna_stran(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/leto_ustanovitve/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_leto_ustanovitve(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/fakultete/univerza/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    fakultete = isci_fakulteta_univerza(iskalni_niz)
    return template('rezultati_iskanja_fakultete', iskalni_niz = iskalni_niz, fakultete = fakultete)

@route('/programi/naziv/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    programi = isci_program_naziv(iskalni_niz)
    return template('rezultati_iskanja_programi', iskalni_niz = iskalni_niz, programi = programi)

@route('/programi/redni/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    programi = isci_program_redni(iskalni_niz)
    return template('rezultati_iskanja_programi', iskalni_niz = iskalni_niz, programi = programi)

@route('/programi/izredni/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    programi = isci_program_izredni(iskalni_niz)
    return template('rezultati_iskanja_programi', iskalni_niz = iskalni_niz, programi = programi)

@route('/programi/stopnja/rezultati/')
def isci():
    iskalni_niz = request.query['iskalni_niz']
    programi = isci_program_stopnja(iskalni_niz)
    return template('rezultati_iskanja_programi', iskalni_niz = iskalni_niz, programi = programi)

@route('/programi/fakulteta/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    programi = isci_program_fakulteta(iskalni_niz)
    return template('rezultati_iskanja_programi', iskalni_niz = iskalni_niz, programi = programi)

@route('/programi/univerza/rezultati/')
def isci():
    iskalni_niz = request.query.iskalni_niz
    programi = isci_program_univerza(iskalni_niz)
    return template('rezultati_iskanja_programi', iskalni_niz = iskalni_niz, programi = programi)

run(debug = True)

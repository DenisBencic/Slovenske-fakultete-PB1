from bottle import route, run, template
from uvoz import uvozi
from iskalne_funkcije import *

param = uvozi()

@route('/')
def pozdrav():
    return template('zacetna_stran.html').format(param[0], param[1], param[2])

@route('/univerze/')
def univerze():

    @route('/univerze/naziv/')
    def naziv():
        return template('isci.html')

    @route('/univerze/tip/')
    def tip():
        return template('isci.html')

    @route('/univerze/rektor/')
    def rektor():
        return template('isci.html')

    @route('/univerze/kontakt/')
    def kontakt():
        return template('isci.html')

    @route('/univerze/e_naslov/')
    def e_naslov():
        return template('isci.html')

    @route('/univerze/spletna_stran/')
    def spletna_stran():
        return template('isci.html')

    @route('/univerze/leto_ustanovitve/')
    def leto_ustanovitve():
        return template('isci.html')

    return template('univerze.html')

@route('/fakultete/')
def fakultete():

    @route('/fakultete/naziv/')
    def naziv():
        return template('isci.html')

    @route('/fakultete/dekan/')
    def dekan():
        return template('isci.html')

    @route('/fakultete/lokacija/')
    def lokacija():
        return template('isci.html')

    @route('/fakultete/kontakt/')
    def kontakt():
        return template('isci.html')

    @route('/fakultete/e_naslov/')
    def e_naslov():
        return template('isci.html')

    @route('/fakultete/spletna_stran/')
    def spletna_stran():
        return template('isci.html')

    @route('/fakultete/leto_ustanovitve/')
    def leto_ustanovitve():
        return template('isci.html')

    @route('/fakultete/univerza/')
    def univerza():
        return template('isci.html')
    
    return template('fakultete.html')

@route('/programi/')
def programi():

    @route('/programi/naziv/')
    def naziv():
        return template('isci.html')

    @route('/programi/redni/')
    def redni():
        return template('isci.html')

    @route('/programi/izredni/')
    def izredni():
        return template('isci.html')

    @route('/programi/stopnja/')
    def stopnja():
        return template('isci.html')

    @route('/programi/fakulteta/')
    def fakulteta():
        return template('isci.html')

    return template('programi.html')

@route('/isci/')
def isci():
    return

run(debug = True)

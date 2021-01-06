import sqlite3 as dbapi

# Univerze

def isci_univerza_naziv(naziv):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podan naziv.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE naziv LIKE '%{}%'".format(naziv))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_univerza_tip(tip):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podan tip.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE tip LIKE '%{}%'".format(tip))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_univerza_rektor(rektor):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podanega rektorja.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE rektor LIKE '%{}%'".format(rektor))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_univerza_lokacija(lokacija):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podano lokacijo.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE lokacija LIKE '%{}%'".format(lokacija))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_univerza_e_naslov(e_naslov):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podan e-naslov.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE e_naslov LIKE '%{}%'".format(e_naslov))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_univerza_spletna_stran(spletna_stran):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podano spletno stran.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE spletna_stran LIKE '%{}%'".format(spletna_stran))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_univerza_leto_ustanovitve(leto_ustanovitve):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podano leto ustanovtive.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE leto_ustanovitve LIKE {}".format(leto_ustanovitve))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

# Fakultete

def isci_fakulteta_naziv(naziv):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podan naziv.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.naziv LIKE '%{}%'".format(naziv))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_dekan(dekan):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podanega dekana.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.dekan LIKE '%{}%'".format(dekan))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_lokacija(lokacija):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano lokacijo.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.lokacija LIKE '%{}%'".format(lokacija))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_kontakt(kontakt):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podan kontakt.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.kontakt LIKE '%{}%'".format(kontakt))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_e_naslov(e_naslov):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podan e-naslov.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.e_naslov LIKE '%{}%'".format(e_naslov))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_spletna_stran(spletna_stran):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano spletno stran.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.spletna_stran LIKE '%{}%'".format(spletna_stran))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_leto_ustanovitve(leto_ustanovitve):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano spletno stran.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE leto_ustanovitve LIKE {}'".format(leto_ustanovitve))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_fakulteta_univerza(naziv):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano spletno stran.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE univerza.naziv LIKE '%{}%'".format(naziv))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

# Programi

def isci_program_naziv(naziv):
    '''
    V bazi poišče program
    in njegove podatke
    glede na podan naziv.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.naziv LIKE '%{}%'".format(naziv))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_program_redni(redni):
    '''
    V bazi poišče program
    in njegove podatke
    glede, ali gre za redni
    program ali ne.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.redni LIKE 1".format(redni))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_program_izredni(izredni):
    '''
    V bazi poišče program
    in njegove podatke
    glede na to, ali gre za redni
    program ali ne.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.izredni LIKE 1".format(izredni))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_program_stopnja(stopnja):
    '''
    V bazi poišče program
    in njegove podatke
    glede na podano stopnjo.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.stopnja LIKE '%{}%'".format(izredni))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni

def isci_program_fakulteta(naziv):
    '''
    V bazi poišče program
    in njegove podatke
    glede na podano stopnjo.
    '''
    povezava = dbapi.connect('SlovenskeFakultete.sqlite')
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.naziv LIKE '%{}%'".format(naziv))
    vrni = kurzor.fetchall()
    povezava.commit()
    kurzor.close()
    povezava.close()
    return vrni
    

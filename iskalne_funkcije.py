import sqlite3 as dbapi
povezava = dbapi.connect('SlovenskeFakultete.sqlite')

# Univerze

def isci_univerza_naziv(naziv):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podan naziv.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE naziv LIKE ?", ['%' + naziv + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_univerza_tip(tip):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podan tip.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE tip LIKE ?", ['%' + tip + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_univerza_rektor(rektor):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podanega rektorja.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE rektor LIKE ?", ['%' + rektor + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_univerza_lokacija(lokacija):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podano lokacijo.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE lokacija LIKE ?", ['%' + lokacija + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_univerza_e_naslov(e_naslov):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podan e-naslov.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE e_naslov LIKE ?", ['%' + e_naslov + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_univerza_spletna_stran(spletna_stran):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podano spletno stran.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE spletna_stran LIKE ?", ['%' + spletna_stran + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_univerza_leto_ustanovitve(leto_ustanovitve):
    '''
    V bazi poišče univerzo
    in njene podatke
    glede na podano leto ustanovtive.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM univerza WHERE leto_ustanovitve = ?", [leto_ustanovitve])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

# Fakultete

def isci_fakulteta_naziv(naziv):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podan naziv.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.naziv LIKE ?", ['%' + naziv + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_dekan(dekan):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podanega dekana.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.dekan LIKE ?", ['%' + dekan + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_lokacija(lokacija):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano lokacijo.
    '''
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.lokacija LIKE ?", ['%' + lokacija + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_kontakt(kontakt):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podan kontakt.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.kontakt LIKE ?", ['%' + kontakt + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_e_naslov(e_naslov):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podan e-naslov.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.e_naslov LIKE ?", ['%' + e_naslov + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_spletna_stran(spletna_stran):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano spletno stran.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.spletna_stran LIKE ?", ['%' + spletna_stran + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_leto_ustanovitve(leto_ustanovitve):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano spletno stran.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE leto_ustanovitve LIKE ?", [leto_ustanovitve])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_fakulteta_univerza(naziv):
    '''
    V bazi poišče fakulteto
    in njene podatke
    glede na podano spletno stran.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * from fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE univerza.naziv LIKE ?", ['%' + naziv + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

# Programi

def isci_program_naziv(naziv):
    '''
    V bazi poišče program
    in njegove podatke
    glede na podan naziv.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.naziv LIKE ?", ['%' + naziv + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_program_redni(redni):
    '''
    V bazi poišče program
    in njegove podatke
    glede, ali gre za redni
    program ali ne.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.redni LIKE ?", [redni])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_program_izredni(izredni):
    '''
    V bazi poišče program
    in njegove podatke
    glede na to, ali gre za redni
    program ali ne.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.izredni LIKE ?", [izredni])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_program_stopnja(stopnja):
    '''
    V bazi poišče program
    in njegove podatke
    glede na podano stopnjo.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE program.stopnja LIKE ?", ['%' + stopnja + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

def isci_program_fakulteta(naziv):
    '''
    V bazi poišče program
    in njegove podatke
    glede na podano stopnjo.
    '''
    kurzor = povezava.cursor()
    kurzor.execute("SELECT * FROM program JOIN fakulteta ON fakulteta.id = program.fakulteta JOIN univerza ON univerza.id = fakulteta.univerza WHERE fakulteta.naziv LIKE ?", ['%' + naziv + '%'])
    vrni = kurzor.fetchall()
    kurzor.close()
    return vrni

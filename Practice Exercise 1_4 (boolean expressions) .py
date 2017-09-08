#Practice Exercise 1_4 (boolean expressions)

a = 6
b = 7
inventaris = ['papier', 'nietjes', 'pennen']
voornaam = 'Jesse'
tussenvoegsel = ''
achternaam = 'Jagers'


if tussenvoegsel is '':
    mijnNaam = voornaam + ' ' + achternaam
else:
    mijnNaam = voornaam + ' ' + tussenvoegsel + ' ' + achternaam

print(mijnNaam)

BiggerorSmaller = 6.75 > a and 6.75 <b
print ('6.75 is groter dan a en kleiner dan b' + (' = ') +  str(BiggerorSmaller)         )

inventaris_count = len(inventaris) > 5*len(mijnNaam)
print ('Is de lengte meer dan 5 keer zo groot dan de lengte van de variabele mijnnaam?' +  (' = ') + str(inventaris_count)    )

inventaris_empty = 0 == len(inventaris)
print('Is de lijst inventaris leeg?' + ' ' + str(inventaris_empty) )

inventaris_ten = len(inventaris) > 10
print ('De lijst van inventaris bevat meer dan 10 items' + (' = ') + str(inventaris_ten) )
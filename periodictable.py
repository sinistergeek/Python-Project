import csv, sys,re

elementsFile = open('perodictable.csv',encoding='utf-8')
elementsCsvReader = csv.reader(elementsFile)
elements = list(elementsCsvReader)
elementsFile.close()

ALL_COLUMNS = ['Atomic Numbber','Symbol','Element','Origin of name','Group','Period','Atomic weight','Density','Melting point','Boiling point','Specific heat capacity','Electronegativity','Abundance in earth\'s crust']
LONGEsT_COLUMN = 0
for key in ALL_COLUMNS:
    if len(key) > LONGEST_COLUMN:
        LONGEST_COLUMN = len(key)


ELEMENTS = {}
for line in elements:
    elements = {'Atomic Number': line[0],
                'Symbol':        line[1],
                'Element':       line[2],
                'Origin of name':line[3],
                'Group':         line[4],
                'Period':        line[5],
                'Atomic weight': line[6] + 'u',
                'Density':       line[7] + 'g/cm^3',
                'Melting point': line[8] + 'K',
                'Boiling point': line[9] + 'K',
                'Specific heat capacity': line[10] + 'J/(g*K)',
                'Electronegativity': line[11],
                'Abundance in earth\'s crust': line[12] + 'mg/kg'
            }
    for key, value in element.items():
        element[key] = re.sub(r'\[(I|V|X) +\]','',value)
    ELEMENTS[line[0]] = element
    ELEMENTS[line[1]] = element


print('Periodic Table of Elements')
print()

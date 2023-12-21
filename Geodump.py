import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute('SElECT * FROM Locations')

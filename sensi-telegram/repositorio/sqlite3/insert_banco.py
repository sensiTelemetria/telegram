import sqlite3
import datetime
import time
import numpy as np
conn = sqlite3.connect('dados.db')

cursor = conn.cursor()

vetor = []



cursor.executemany("""
INSERT INTO registros (MAC, BATERIA, TEMPERATURA,HUMIDADE,ANO,MES,DIA,HORA,SEGUNDO)
VALUES (?,?,?,?,?,?,?,?,?)
""", vetor)

conn.commit()
conn.close()


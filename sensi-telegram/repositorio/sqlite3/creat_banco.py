import sqlite3
conn = sqlite3.connect('home/pi/Desktop/sensi.db')

cursor = conn.cursor()

#ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,

cursor.execute("""
CREATE TABLE reg (
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        MAC TEXT NOT NULL,
        BATERIA INTEGER NOT NULL,
        TEMPERATURA DOUBLE NOT NULL,
        UMIDADE DOUBLE NOT NULL,
        ANO INTEGER NOT NULL ,
        MES INTEGER NOT NULL ,
        DIA INTEGER NOT NULL ,
        HORA INTEGER NOT NULL ,
        MINUTO INTEGER NOT NULL ,
        SEGUNDO INTEGER NOT NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...

# criando a tabela (schema)

conn.close()


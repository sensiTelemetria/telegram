#import matplotlib.pyplot as plt
#import numpy as np
from settings import tempDir, dataBaseDjangoDir, dataBaseSensiDir
import sqlite3

class Graphics:

    def getInfo(self):
        msg = ', aqui estão os gráficos de suas SensiTags do '
        return  msg

    def getSensiTags(self):
        conn = sqlite3.connect(dataBaseDjangoDir)
        cursor = conn.cursor()
        cursor.execute("""select * from tags_tag""")
        conn.commit()
        query = (cursor.fetchall())
        return query

    def graphic(self, numberRegs, chat_id):

        print(self.getSensiTags())


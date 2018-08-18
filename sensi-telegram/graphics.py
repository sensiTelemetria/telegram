import matplotlib.pyplot as plt
import numpy as np
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

        x = np.linspace(0, 2 * np.pi, 400)
        y = np.sin(x ** 2)
        plt.close('all')
        # Four axes, returned as a 2-d array
        f, axarr = plt.subplots(2, 2)
        axarr[0, 0].plot(x, y)
        axarr[0, 0].set_title('Axis [0,0]')
        axarr[0, 1].scatter(x, y)
        axarr[0, 1].set_title('Axis [0,1]')
        axarr[1, 0].plot(x, y ** 2)
        axarr[1, 0].set_title('Axis [1,0]')
        axarr[1, 1].scatter(x, y ** 2)
        axarr[1, 1].set_title('Axis [1,1]')
        # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
        plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
        plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
        plt.show()
        f.savefig(tempDir+'teste.png')

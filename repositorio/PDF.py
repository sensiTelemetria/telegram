import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

with PdfPages('multipage.pdf') as pp:
    fig = plt.figure()

    fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
    pp.savefig(fig)

    for i in range(0, 15):
        fig = plt.figure()
        x = np.linspace(0, 1000)
        plt.plot(x, np.sin(x * i * np.pi / 1),linewidth = 2.5,label = "linha teste")
        plt.title("gráfico "+ str(i))
        plt.grid()
        plt.legend()
        pp.savefig(fig)